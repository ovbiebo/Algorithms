class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}


function find_maximum_path_sum(root) {
    let result = 0;
    function calculate_path_sum(node){
        if (!node) return 0;
        let left_sum = Math.max(calculate_path_sum(node.left), 0);
        let right_sum = Math.max(calculate_path_sum(node.right), 0);
        let path_sum = node.val + left_sum + right_sum;
        result = Math.max(path_sum, result) || path_sum;
        return node.val + Math.max(left_sum, right_sum);
    }

    calculate_path_sum(root);
    return result;
}

let root = new TreeNode(1)
root.left = new TreeNode(2)
root.right = new TreeNode(3)
console.log(`Maximum Path Sum: ${find_maximum_path_sum(root)}`)

root.left.left = new TreeNode(1)
root.left.right = new TreeNode(3)
root.right.left = new TreeNode(5)
root.right.right = new TreeNode(6)
root.right.left.left = new TreeNode(7)
root.right.left.right = new TreeNode(8)
root.right.right.left = new TreeNode(9)
console.log(`Maximum Path Sum: ${find_maximum_path_sum(root)}`)

root = new TreeNode(-1)
root.left = new TreeNode(-3)
console.log(`Maximum Path Sum: ${find_maximum_path_sum(root)}`)
