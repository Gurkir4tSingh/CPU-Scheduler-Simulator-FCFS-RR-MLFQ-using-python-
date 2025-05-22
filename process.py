class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = None

    def reset(self):
        self.remaining_time = self.burst_time
        self.start_time = None
        self.completion_time = None
