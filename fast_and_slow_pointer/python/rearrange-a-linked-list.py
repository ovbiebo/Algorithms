class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    left_of_slow = None
    while slow:
        slow, left_of_slow = reverse_nodes(slow, left_of_slow)

    slow = head
    fast = left_of_slow

    while slow.next != fast and fast != slow:
        _ = slow
        slow = slow.next
        _.next = fast
        _ = fast
        fast = fast.next
        _.next = slow

    return


def reverse_nodes(leading: Node, trailing):
    _ = leading
    leading = leading.next
    _.next = trailing
    trailing = _
    return leading, trailing


if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()
