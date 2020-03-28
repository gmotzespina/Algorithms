class ListNode {
 constructor(public value: number, public next: ListNode|null = null ){}
}

const head = new ListNode(1);
const newNode = new ListNode(2);

head.next = newNode;

console.log(head.value);
console.log(head.next.value);
