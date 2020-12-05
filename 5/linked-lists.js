
class IntNode {
    constructor(n) {
        this.n = n;
        this.next = null;
    }
}
class LinkedListOfInts {
    constructor() {
        this.firstNode = null;
    }
    add(n) {
        const node = new IntNode(n);
        if (!this.firstNode) {
            this.firstNode = node;
            return;
        }
        if (this.firstNode.n > node.n) {
            node.next = this.firstNode;
            this.firstNode = node;
            return;
        }
        let current = this.firstNode;
        while (current.next && current.next.n < node.n) {
            current = current.next;
        }
        const prevNext = current.next;
        current.next = node;
        node.next = prevNext;
    }
    forEachInt(f) {
        let current = this.firstNode;
        while (current) {
            f(current.n);
            current = current.next;
        }
    }
    toArray() {
        let a = [];
        this.forEachInt((n) => a[a.length] = n);
        return a;
    }
    print() {
        this.forEachInt((n) => console.log(n));
    }
}

exports.LinkedListOfInts = LinkedListOfInts;
