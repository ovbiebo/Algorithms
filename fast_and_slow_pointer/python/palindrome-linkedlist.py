class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    slow = fast = head
    left_of_slow = None

    while fast and fast.next:
        fast = fast.next.next
        slow, left_of_slow = reverse_nodes(slow, left_of_slow)

    fast = slow if fast is None else slow.next

    while fast:
        if fast.value != left_of_slow.value:
            return False
        fast = fast.next
        left_of_slow, slow = reverse_nodes(left_of_slow, slow)

    return True


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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    print(f"Is palindrome: {is_palindromic_linked_list(head)}")

    head.next.next.next.next.next = Node(2)
    print(f"Is palindrome: {is_palindromic_linked_list(head)}")
