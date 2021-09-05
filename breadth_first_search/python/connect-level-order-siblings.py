from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.val) + " ", end='')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()


def connect_level_order_siblings(root: TreeNode):
    if root is None:
        return

    queue = deque()
    queue.append({'node': root, 'level': 0})

    while queue:
        node, level = queue.popleft().values()
        if queue and queue[0]['level'] == level:
            node.next = queue[0]['node']

        if node.left:
            queue.append({'node': node.left, 'level': level + 1})
        if node.right:
            queue.append({'node': node.right, 'level': level + 1})


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer are: ")
    root.print_level_order()


main()
