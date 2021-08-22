class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    get_interval() {
        return "[" + this.start + ", " + this.end + "]";
    }
}

const find_employee_free_time = (intervals) => {
    let result = [];
    let combinedIntervals = [];

    for (const employeeIntervals of intervals) {
        combinedIntervals.push(...employeeIntervals)
    }

    combinedIntervals.sort((a, b) => a.start - b.start)

    for (let i = 1; i < combinedIntervals.length; i++) {
        if (combinedIntervals[i - 1].end < combinedIntervals[i].start) {
            result.push(new Interval(combinedIntervals[i - 1].end, combinedIntervals[i].start))
        }
    }

    return result;
}

let intervals = find_employee_free_time([
    [new Interval(1, 3), new Interval(5, 6)],
    [new Interval(2, 3), new Interval(6, 8)]
]);
let result = "Free intervals: ";
for (let i = 0; i < intervals.length; i++) {
    result += intervals[i].get_interval();
}
console.log(result); // [[3, 5]]

intervals = find_employee_free_time([
    [new Interval(1, 3), new Interval(9, 12)],
    [new Interval(2, 4)],
    [new Interval(6, 8)]
]);
result = "Free intervals: ";
for (let i = 0; i < intervals.length; i++) {
    result += intervals[i].get_interval();
}
console.log(result); // [[4, 6], [8, 9]]

intervals = find_employee_free_time([
    [new Interval(1, 3)],
    [new Interval(2, 4)],
    [new Interval(3, 5), new Interval(7, 9)]
]);
result = "Free intervals: ";
for (let i = 0; i < intervals.length; i++) {
    result += intervals[i].get_interval();
}
console.log(result); // [[5, 7]]
