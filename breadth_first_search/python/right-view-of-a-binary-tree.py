from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)


def tree_right_view(root: TreeNode) -> list:
    if root is None:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if _ + 1 == level_size:
                result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print(result)


main()
