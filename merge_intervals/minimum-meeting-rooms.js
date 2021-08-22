class Meeting {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }
}

const min_meeting_rooms = (meetings) => {
    let result = 1;
    let concurrentMeetings = 1;
    let back = 0;
    let front = 1;

    meetings.sort((a, b) => a.end - b.end);

    while (front < meetings.length) {
        while (back < front) {
            concurrentMeetings = front - back + 1;
            if (meetings[front].start < meetings[back].end) {
                result = Math.max(concurrentMeetings, result);
                break;
            } else {
                back++
            }
        }
        front++
    }

    return result;
}

console.log(`Minimum meeting rooms required: ${min_meeting_rooms([
    new Meeting(1, 4), new Meeting(2, 5), new Meeting(7, 9),
])}`); // 2
console.log(`Minimum meeting rooms required: ${min_meeting_rooms([
    new Meeting(6, 7), new Meeting(2, 4), new Meeting(8, 12),
])}`); // 1
console.log(`Minimum meeting rooms required: ${min_meeting_rooms([
    new Meeting(1, 4), new Meeting(2, 3), new Meeting(3, 6),
])}`); // 2
console.log(`Minimum meeting rooms required: ${min_meeting_rooms([
    new Meeting(4, 5), new Meeting(2, 3), new Meeting(2, 4), new Meeting(3, 5),
])}`); // 2
