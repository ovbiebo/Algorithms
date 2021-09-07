class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

const find_paths = (root) => {
    const dfs = (node, number_so_far = 0) => {
        if (!node) return 0;
        number_so_far = number_so_far * 10 + node.value;
        if (!node.left && !node.right) return number_so_far;
        return dfs(node.left, number_so_far) + dfs(node.right, number_so_far)
    }

    return dfs(root);
}

let root = new TreeNode(1);
root.left = new TreeNode(0);
root.right = new TreeNode(1);
root.left.left = new TreeNode(1);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(5);
console.log(`Total Sum of Path Numbers: ${find_paths(root)}`);