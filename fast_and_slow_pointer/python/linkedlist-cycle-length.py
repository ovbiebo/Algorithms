class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head):
    slow = fast = head
    length = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                length += 1
                if slow == fast:
                    return length

    return length


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(f"LinkedList has cycle: {find_cycle_length(head)}")

    head.next.next.next.next.next.next = head.next.next
    print(f"LinkedList has cycle: {find_cycle_length(head)}")

    head.next.next.next.next.next.next = head.next.next.next
    print(f"LinkedList has cycle: {find_cycle_length(head)}")
