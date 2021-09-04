class TreeNode {
    constructor(val) {
        this.val = val;
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

    get length (){
        return this.front - this.back;
    }

    peek(){
        return this.items[this.back];
    }

    enqueue(item){
        this.items[this.front] = item;
        this.front++;
    }

    dequeue(){
        let item = this.peek();
        delete this.items[this.back];
        this.back++;
        return item;
    }
}

const find_successor = (root, key) => {
    if (!root) return null;

    let queue = new Queue();
    queue.enqueue(root)

    while (queue.length > 0) {
        let currNode = queue.dequeue();
        currNode.left && queue.enqueue(currNode.left);
        currNode.right && queue.enqueue(currNode.right);
        if (currNode.val === key) return queue.peek();
    }
    return null;
}

let root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);

let result = find_successor(root, 12)
if(result != null) console.log(result.val)

result = find_successor(root, 9)
if(result != null) console.log(result.val)
