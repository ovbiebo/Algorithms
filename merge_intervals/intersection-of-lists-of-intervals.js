class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    print_interval() {
        process.stdout.write("[" + this.start + ", " + this.end + "]");
    }
}

const merge = (intervals_a, intervals_b) => {
    let merged = [];
    let a = 0,
        b = 0;

    while (intervals_a[a]) {
        while (intervals_b[b] && intervals_b[b].end < intervals_a[a].start) {
            b++;
        }

        while (intervals_a[a].start <= intervals_b[b]?.end && intervals_a[a].end >= intervals_b[b]?.start) {
            merged.push(new Interval(
                Math.max(intervals_a[a].start, intervals_b[b].start),
                Math.min(intervals_a[a].end, intervals_b[b].end)
            ))
            if (intervals_b[b].end > intervals_a[a].end) break;
            b++;
        }

        a++;
    }

    return merged;
}

process.stdout.write(`Intervals intersection: `);
let result = merge(
    [new Interval(1, 3), new Interval(5, 6), new Interval(7, 9)],
    [new Interval(2, 3), new Interval(5, 7)]
);
for (let i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();

process.stdout.write(`Intervals intersection: `);
result = merge(
    [new Interval(1, 3), new Interval(5, 7), new Interval(9, 12)],
    [new Interval(5, 10)]
);
for (let i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();
