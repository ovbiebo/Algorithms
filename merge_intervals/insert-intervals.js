class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    print_interval() {
        process.stdout.write("[" + this.start + ", " + this.end + "]");
    }
}

const insert = (intervals, new_interval) => {
    let merged = [];
    let i = 0;

    while (intervals[i] && intervals[i].end < new_interval.start) {
        merged.push(intervals[i]);
        i++;
    }

    while (new_interval.start <= intervals[i]?.end && new_interval.end >= intervals[i]?.start) {
        new_interval.start = Math.min(new_interval.start, intervals[i].start);
        new_interval.end = Math.max(new_interval.end, intervals[i].end);
        i++;
    }

    merged.push(new_interval)

    while (intervals[i]) {
        merged.push(intervals[i]);
        i++;
    }

    return merged;
}

process.stdout.write(`Intervals after inserting the new intervals: `);
let result = insert([
    new Interval(1, 3),
    new Interval(5, 7),
    new Interval(8, 12),
], new Interval(4, 6));
for (let i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();

process.stdout.write(`Intervals after inserting the new intervals: `);
result = insert([
    new Interval(1, 3),
    new Interval(5, 7),
    new Interval(8, 12),
], new Interval(4, 10));
for (let i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();

process.stdout.write(`Intervals after inserting the new intervals: `);
result = insert([
    new Interval(2, 3),
    new Interval(5, 7)
], new Interval(1, 4));
for (let i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();
