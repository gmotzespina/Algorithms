var Leaf = /** @class */ (function () {
    function Leaf(value, left, right) {
        if (left === void 0) { left = null; }
        if (right === void 0) { right = null; }
        this.value = value;
        this.left = left;
        this.right = right;
    }
    return Leaf;
}());
var Tree = /** @class */ (function () {
    function Tree(root) {
        this.root = root;
    }
    Tree.prototype.push = function (node, root) {
        if (root === void 0) { root = this.root; }
        if (root.value >= node.value) {
            if (root.left) {
                this.push(node, root.left);
            }
            else {
                root.left = node;
            }
        }
        else {
            if (root.right) {
                this.push(node, root.right);
            }
            else {
                root.right = node;
            }
        }
    };
    Tree.prototype.dfs = function (searchedValue, root) {
        if (root === void 0) { root = this.root; }
        if (!root) {
            console.log('Inexistent value');
            return;
        }
        if (searchedValue === root.value) {
            console.log('Value found', root.value);
            return;
        }
        if (searchedValue > root.value) {
            this.dfs(searchedValue, root.right);
        }
        else {
            this.dfs(searchedValue, root.left);
        }
    };
    Tree.prototype.dfPreorderTraversal = function (root) {
        if (root === void 0) { root = this.root; }
        console.log(root.value);
        if (root.left) {
            this.dfPreorderTraversal(root.left);
        }
        if (root.right) {
            this.dfPreorderTraversal(root.right);
        }
    };
    Tree.prototype.dfInorderTraversal = function (root) {
        if (root === void 0) { root = this.root; }
        if (root.left) {
            this.dfInorderTraversal(root.left);
        }
        console.log(root.value);
        if (root.right) {
            this.dfInorderTraversal(root.right);
        }
    };
    return Tree;
}());
var tree = new Tree(new Leaf(1));
var node1 = new Leaf(3);
var node2 = new Leaf(2);
var node3 = new Leaf(4);
tree.push(new Leaf(0));
tree.push(node1);
tree.push(node2);
tree.push(node3);
tree.push(new Leaf(5));
// tree.push(new Leaf(-2));
// tree.push(new Leaf(-1));
// tree.push(new Leaf(4));
// console.log('Root: ', tree.root.value);
// console.log('Right: ', tree.root.right.value);
// console.log('Tree: ', tree.root.left.value);
// console.log('Right: ', tree.root.right.left.value);
tree.dfs(3);
tree.dfs(0);
tree.dfs(1);
tree.dfs(2);
console.log('Preorder: ');
tree.dfPreorderTraversal();
console.log('Inorder: ');
tree.dfInorderTraversal();
