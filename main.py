from process import Process
from fcfs import fcfs_scheduler
from rr import rr_scheduler
from mlfq import mlfq_scheduler
import matplotlib.pyplot as plt

#Gantt Chart Drawer
def draw_gantt_chart(timeline, title="Gantt Chart"):
    fig, gnt = plt.subplots()
    gnt.set_title(title)
    gnt.set_xlabel("Time")
    gnt.set_ylabel("Processes")

    process_ids = list({item[0] for item in timeline})
    process_ids.sort()

    gnt.set_yticks([15 + 10 * i for i in range(len(process_ids))])
    gnt.set_yticklabels(process_ids)
    gnt.set_ylim(0, 10 * len(process_ids) + 10)
    gnt.grid(True)

    colors = plt.cm.get_cmap("tab20", len(process_ids))

    for i, pid in enumerate(process_ids):
        y_pos = 10 * i + 10
        for start, end in [(s, e) for p, s, e in timeline if p == pid]:
            gnt.broken_barh([(start, end - start)], (y_pos, 8), facecolors=colors(i))

    plt.show()

#Sample processes
processes = [
    Process(pid="P1", arrival_time=0, burst_time=5),
    Process(pid="P2", arrival_time=1, burst_time=3),
    Process(pid="P3", arrival_time=2, burst_time=8),
]

#Reset for FCFS
print("Running FCFS:")
timeline_fcfs = fcfs_scheduler(processes)
draw_gantt_chart(timeline_fcfs, "FCFS Scheduler")

#Reset for RR
for p in processes:
    p.reset()
print("Running Round Robin:")
timeline_rr = rr_scheduler(processes, time_quantum=2)
draw_gantt_chart(timeline_rr, "Round Robin Scheduler (Time Quantum = 2)")

#Reset for MLFQ
for p in processes:
    p.reset()
print("Running MLFQ:")
timeline_mlfq = mlfq_scheduler(processes, queues=3, time_quantums=[2, 4, 6])
draw_gantt_chart(timeline_mlfq, "MLFQ Scheduler (3 Queues)")
