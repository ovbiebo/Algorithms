class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow = fast = head

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    length = 0
    while True:
        slow = slow.next
        fast = fast.next.next
        length += 1
        if slow == fast:
            break

    slow = fast = head
    while length:
        fast = fast.next
        length -= 1

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print(f"LinkedList has cycle: {find_cycle_start(head).value}")

    head.next.next.next.next.next.next = head.next.next.next
    print(f"LinkedList has cycle: {find_cycle_start(head).value}")

    head.next.next.next.next.next.next = head
    print(f"LinkedList has cycle: {find_cycle_start(head).value}")
