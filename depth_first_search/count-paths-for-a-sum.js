class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function find_paths(root, S) {
    function dfs(node, path = []) {
        if (!node) return 0;
        path.push(node.value);
        let [path_sum, total] = [0, 0];
        for (let i = path.length - 1; i >= 0; i--) {
            path_sum += path[i];
            if (path_sum === S) total++;
        }
        total += dfs(node.left, path) + dfs(node.right, path)
        path.pop();
        return total;
    }

    return dfs(root, [])
}

root = new TreeNode(5)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(4)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
root.right.left.left = new TreeNode(1)
console.log(`Tree has paths: ${find_paths(root, 11)}`)
