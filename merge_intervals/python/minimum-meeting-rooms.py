class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda meeting: meeting.start)
    meetings.sort(key=lambda meeting: meeting.end)

    back = 0
    rooms = 1

    for front in range(1, len(meetings)):
        while meetings[front].start >= meetings[back].end:
            back += 1
        rooms = max(rooms, front - back + 1)

    return rooms


if __name__ == '__main__':
    print(f"Minimum meeting rooms required: {min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])}")
    print(f"Minimum meeting rooms required: {min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])}")
    print(f"Minimum meeting rooms required: {min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])}")
    print(
        f"Minimum meeting rooms required: {min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])}")
