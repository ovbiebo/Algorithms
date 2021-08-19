class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    get_interval() {
        return "[" + this.start + ", " + this.end + "]";
    }
}

const merge = (intervals) => {
    let merged = [];
    let i = 0;

    intervals.sort((a, b) => a.start - b.start);

    while (i < intervals.length) {
        let temp = intervals[i];
        i++;

        while (intervals[i] && intervals[i].start < temp.end) {
            temp = new Interval(temp.start, Math.max(temp.end, intervals[i].end));
            i++;
        }
        merged.push(temp);
    }

    return merged;
}

let merged_intervals = merge([new Interval(1, 4), new Interval(2, 5), new Interval(7, 9)]);
let result = "";
for (let i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`); // [[1, 5], [7, 9]]

merged_intervals = merge([new Interval(6, 7), new Interval(2, 4), new Interval(5, 9)]);
result = "";
for (let i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`); // [[2, 4], [5, 9]]

merged_intervals = merge([new Interval(1, 4), new Interval(2, 6), new Interval(3, 5)]);
result = "";
for (let i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`); // [[1, 6]]
