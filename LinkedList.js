class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  append(data) {
    const newNode = new Node(data);
    if (!this.head) {
      this.head = this.tail = newNode;
      return;
    }
    this.tail.next = newNode;
    this.tail = newNode;
  }

  printList() {
    let currentNode = this.head;
    while (currentNode) {
      console.log(currentNode.data);
      currentNode = currentNode.next;
    }
    console.log("None");
  }

  isEmpty() {
    return this.head === null;
  }

  reverse() {
    let prevNode = null;
    let currentNode = this.head;
    while (currentNode) {
      const nextNode = currentNode.next;
      currentNode.next = prevNode;
      prevNode = currentNode;
      currentNode = nextNode;
    }
    this.head = prevNode;
  }
}

// Example usage:
const myList = new LinkedList();
myList.append(1);
myList.append(2);
myList.append(9);
myList.append(4);

// Printing the linked list
console.log("Original Linked List:");
myList.printList();

// Reversing the linked list
myList.reverse();

console.log("\nReversed Linked List:");
myList.printList();
