from collections import deque

def mlfq_scheduler(processes, queues, time_quantums):
    levels = [deque() for _ in range(queues)]
    processes = sorted(processes, key=lambda p: p.arrival_time)
    time = 0
    i = 0
    timeline = []

    while any(levels) or i < len(processes):
        while i < len(processes) and processes[i].arrival_time <= time:
            levels[0].append(processes[i])
            i += 1

        for level in range(queues):
            if levels[level]:
                p = levels[level].popleft()
                if p.start_time is None:
                    p.start_time = time

                tq = time_quantums[level]
                exec_time = min(tq, p.remaining_time)
                timeline.append((p.pid, time, time + exec_time))
                time += exec_time
                p.remaining_time -= exec_time

                while i < len(processes) and processes[i].arrival_time <= time:
                    levels[0].append(processes[i])
                    i += 1

                if p.remaining_time > 0:
                    if level + 1 < queues:
                        levels[level + 1].append(p)
                    else:
                        levels[-1].append(p)
                else:
                    p.completion_time = time
                break
        else:
            time += 1

    return timeline
