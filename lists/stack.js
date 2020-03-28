var Stack = /** @class */ (function () {
    function Stack(head) {
        var _this = this;
        this.head = head;
        this.length = 1;
        this.pop = function () {
            _this.head = _this.head.next;
        };
        this.push = function (node) {
            var auxNode = _this.head;
            _this.head = node;
            _this.head.next = auxNode;
            _this.length += 1;
        };
        this.printStack = function () {
            var auxNode = _this.head;
            while (auxNode) {
                console.log(auxNode.value);
                auxNode = auxNode.next;
            }
        };
        this.size = function () {
            console.log("Size of stack is: " + _this.length);
        };
    }
    return Stack;
}());
var MyNode = /** @class */ (function () {
    function MyNode(value) {
        this.value = value;
    }
    return MyNode;
}());
var head = new MyNode(1);
var stack = new Stack(head);
var newNode = new MyNode(2);
stack.push(newNode);
stack.size();
// stack.printStack();
stack.push(new MyNode(3));
stack.pop();
stack.push(new MyNode(4));
stack.printStack();
