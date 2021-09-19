class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    l = r = head
    while r and r.next:
        l = l.next
        r = r.next.next
        if l == r:
            return True

    return False


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(f"LinkedList has cycle: {has_cycle(head)}")

    head.next.next.next.next.next.next = head.next.next
    print(f"LinkedList has cycle: {has_cycle(head)}")

    head.next.next.next.next.next.next = head.next.next.next
    print(f"LinkedList has cycle: {has_cycle(head)}")
