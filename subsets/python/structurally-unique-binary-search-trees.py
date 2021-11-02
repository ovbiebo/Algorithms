class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    return find_unique_trees_rec(1, n + 1)


def find_unique_trees_rec(start, end):
    if end == start:
        return [None]

    subtrees = []

    for i in range(start, end):
        left = find_unique_trees_rec(start, i)
        right = find_unique_trees_rec(i + 1, end)
        for l_node in left:
            for r_node in right:
                root = TreeNode(i)
                root.left = l_node
                root.right = r_node
                subtrees.append(root)

    return subtrees


if __name__ == '__main__':
    print(f"Total trees: {len(find_unique_trees(2))}")
    print(f"Total trees: {len(find_unique_trees(3))}")
