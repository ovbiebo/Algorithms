from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)


def traverse(root):
    result = []
    if root is None:
        return result

    should_reverse = False
    queue = deque()
    queue.append(root)

    while queue:
        level = deque()
        level_size = len(queue)

        for i in range(level_size):
            current_node: TreeNode = queue.popleft()
            if should_reverse:
                level.appendleft(current_node)
            else:
                level.append(current_node)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        should_reverse = not should_reverse
        result.append(list(level))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
