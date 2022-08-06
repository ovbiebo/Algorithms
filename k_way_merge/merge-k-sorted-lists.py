from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    min_heap = []
    for head in lists:
        heappush(min_heap, head)

    result_head = result_tail = heappop(min_heap)
    while min_heap:
        if result_tail.next is not None:
            heappush(min_heap, result_tail.next)
        result_tail.next = heappop(min_heap)
        result_tail = result_tail.next

    return result_head


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next
