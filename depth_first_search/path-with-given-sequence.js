class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

const find_path = (root, sequence) => {
    const dfs = (node, level) => {
        if (!node || node.value !== sequence[level]) return false;
        if (!node.left && !node.right && level === sequence.length - 1) return true;
        return dfs(node.left, level + 1) || dfs(node.right, level + 1)
    }
    return dfs(root, 0)
}

let root = new TreeNode(1);
root.left = new TreeNode(0);
root.right = new TreeNode(1);
root.left.left = new TreeNode(1);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(5);

console.log(`Tree has path sequence: ${find_path(root, [1, 0, 7])}`);
console.log(`Tree has path sequence: ${find_path(root, [1, 1, 6])}`);