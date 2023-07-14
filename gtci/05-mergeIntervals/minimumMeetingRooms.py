import heapq


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def minimumMeetingRooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    min_rooms = 0
    min_heap = []
    for meeting in meetings:
        # remove all the meetings that have ended
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heapq.heappop(min_heap)

        # add the current meeting into the min heap
        heapq.heappush(min_heap, meeting)

        # all active meetings are in the min heap, so we need rooms for all of them --
        #   store the max size of the min heap
        min_rooms = max(min_rooms, len(min_heap))

    return min_rooms


def main():
    print(
        "Minimum meeting rooms required: "
        + str(minimumMeetingRooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(minimumMeetingRooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(minimumMeetingRooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(
            minimumMeetingRooms(
                [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]
            )
        )
    )


main()
