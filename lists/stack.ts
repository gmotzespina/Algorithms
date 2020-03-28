
interface NodeProperties {
	value: number;
	next?: NodeProperties;
}

interface StackProperties {
	head?: NodeProperties;
	length: number;
	pop: () => void;
	push: () => void;
	printStack: () => void;
	size: () => void;
}

class Stack<StackProperties> {

	private length = 1;

	constructor(public head?: NodeProperties) {}

	pop = () => {
		this.head = this.head.next;
	}

	push = (node: NodeProperties) => {
		const auxNode = this.head;
		this.head = node;
		this.head.next = auxNode;
		this.length += 1;
	}

	printStack = () => {
		let auxNode = this.head;
		while(auxNode) {
			console.log(auxNode.value);
			auxNode = auxNode.next;
		}
	}

	size = () => {
		console.log(`Size of stack is: ${this.length}`);
	}
}

class MyNode<NodeProperties> {

	constructor(public value: number) {}

}

const head = new MyNode(1)

const stack = new Stack(head);

const newNode = new MyNode(2);

stack.push(newNode);

stack.size();

// stack.printStack();

stack.push(new MyNode(3));

stack.pop();

stack.push(new MyNode(4));

stack.printStack();
