class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda job: job.start)
    jobs.sort(key=lambda job: job.end)

    back = 0
    load = jobs[0].cpu_load
    max_load = load

    for front in range(1, len(jobs)):
        load += jobs[front].cpu_load
        while jobs[front].start >= jobs[back].end:
            load -= jobs[back].cpu_load
            back += 1
        max_load = max(max_load, load)

    return max_load


if __name__ == '__main__':
    print(f"Minimum meeting rooms required: {find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])}")
    print(f"Minimum meeting rooms required: {find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])}")
    print(f"Minimum meeting rooms required: {find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])}")
