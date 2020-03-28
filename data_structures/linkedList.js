var ListNode = /** @class */ (function () {
    function ListNode(value, next) {
        if (next === void 0) { next = null; }
        this.value = value;
        this.next = next;
    }
    return ListNode;
}());
var head = new ListNode(1);
var newNode = new ListNode(2);
head.next = newNode;
console.log(head.value);
console.log(head.next.value);
