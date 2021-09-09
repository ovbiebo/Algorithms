class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_paths(root, S):
    def dfs(node, path) -> int:
        if node is None:
            return 0

        path.append(node.value)
        path_sum = total = 0

        for i in range(len(path) - 1, -1, -1):
            path_sum += path[i]
            if path_sum == S:
                total += 1

        total += dfs(node.left, path) + dfs(node.right, path)

        path.pop()

        return total

    return dfs(root, [])


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(1)
    print(f"Tree has paths: {find_paths(root, 11)}")
