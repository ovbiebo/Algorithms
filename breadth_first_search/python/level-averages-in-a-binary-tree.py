from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)


def find_level_averages(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level = []
        level_size = len(queue)

        for i in range(level_size):
            current_node: TreeNode = queue.popleft()
            level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(level)

    for i, val in enumerate(result):
        result[i] = sum(val)/len(val)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
