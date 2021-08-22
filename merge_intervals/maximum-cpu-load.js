class Job {
    constructor(start, end, cpu_load) {
        this.start = start;
        this.end = end;
        this.cpu_load = cpu_load;
    }
}

const find_max_cpu_load = (jobs) => {
    jobs.sort((a, b) => a.end - b.end);
    let result = jobs[0].cpu_load;
    let currentLoad = result;
    let back = 0;
    let front = 1;


    while (front < jobs.length) {
        while (back < front) {
            if (jobs[front].start < jobs[back].end) {
                break;
            } else {
                currentLoad -= jobs[back].cpu_load;
                back++
            }
        }
        currentLoad += jobs[front].cpu_load;
        result = Math.max(currentLoad, result);
        front++
    }

    return result;
}

console.log(`Maximum CPU load at any time: ${find_max_cpu_load([
    new Job(1, 4, 3), new Job(2, 5, 4), new Job(7, 9, 6),
])}`); // 7
console.log(`Maximum CPU load at any time: ${find_max_cpu_load([
    new Job(6, 7, 10), new Job(2, 4, 11), new Job(8, 12, 15),
])}`); // 15
console.log(`Maximum CPU load at any time: ${find_max_cpu_load([
    new Job(1, 4, 2), new Job(2, 4, 1), new Job(3, 6, 5),
])}`); // 8
