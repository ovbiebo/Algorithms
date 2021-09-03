class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

const traverse = (root) => {
    result = [];
    let queue = [root];

    while (queue.length > 0) {
        let level = [];
        let levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            let currNode = queue.shift();
            level.push(currNode)
            currNode.left && queue.push(currNode.left);
            currNode.right && queue.push(currNode.right);
        }
        result.push(level)
    }
    return result;
}

let root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);

console.log(`Level order traversal: `);
console.log(traverse(root));
