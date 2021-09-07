class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

const find_paths = (root, sum) => {
    let result = []

    const dfs = (node, sum, path = []) => {
        if (!node) return;
        path.push(node.value)
        if (sum - node.value === 0 && !node.left && !node.right) result.push([...path])
        dfs(node.left, sum - node.value, path)
        dfs(node.right, sum - node.value, path)
        path.pop()
    }
    dfs(root, sum);

    return result;
}

let root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(4);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
let sum = 23;
console.log(`Tree paths with sum ${sum}: `);
console.log(find_paths(root, sum));