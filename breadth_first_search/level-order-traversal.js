class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class Queue {
    constructor() {
        this.items = {};
        this.front = 0;
        this.back = 0;
    }

    get length() {
        return this.front - this.back;
    }

    peek() {
        return this.items[this.back];
    }

    enqueue(item) {
        this.items[this.front] = item;
        this.front++;
    }

    dequeue() {
        const item = this.peek();
        delete this.items[this.back];
        this.back++;
        return item;
    }
}

const traverse = (root) => {
    result = [];
    if (!root) return result;

    let queue = new Queue();
    queue.enqueue(root)

    while (queue.length > 0) {
        let level = [];
        let levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            let currNode = queue.dequeue();
            level.push(currNode)
            currNode.left && queue.enqueue(currNode.left);
            currNode.right && queue.enqueue(currNode.right);
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
