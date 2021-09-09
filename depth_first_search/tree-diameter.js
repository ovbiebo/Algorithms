class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class TreeDiameter {
    constructor() {
        this.treeDiameter = 0;
    }

    find_diameter(root) {
        const calculate_height = (node) => {
            if (!node) return 0;
            let [left_height, right_height] = [calculate_height(node.left), calculate_height(node.right)]
            let current_diameter = 1 + left_height + right_height;
            this.treeDiameter = Math.max(current_diameter, this.treeDiameter);
            return 1 + Math.max(left_height, right_height);
        }

        calculate_height(root);
        return this.treeDiameter;
    }
}

let treeDiameter = new TreeDiameter()
let root = new TreeNode(1)
root.left = new TreeNode(2)
root.right = new TreeNode(3)
root.left.left = new TreeNode(4)
root.right.left = new TreeNode(5)
root.right.right = new TreeNode(6)
console.log(`Tree Diameter: ${treeDiameter.find_diameter(root)}`)
root.left.left = null
root.right.left.left = new TreeNode(7)
root.right.left.right = new TreeNode(8)
root.right.right.left = new TreeNode(9)
root.right.left.right.left = new TreeNode(10)
root.right.right.left.left = new TreeNode(11)
console.log(`Tree Diameter: ${treeDiameter.find_diameter(root)}`)
