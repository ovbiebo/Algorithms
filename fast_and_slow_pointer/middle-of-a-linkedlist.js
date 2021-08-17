class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }
}

const find_middle_of_linked_list = function (head) {
    let l = head;
    let r = head.next;

    while (r) {
        r = r.next?.next;
        l = l.next;
    }

    return l;
}

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);

console.log(`LinkedList cycle start: ${find_middle_of_linked_list(head).value}`); // 3

head.next.next.next.next.next = new Node(6);
console.log(`LinkedList cycle start: ${find_middle_of_linked_list(head).value}`); // 4

head.next.next.next.next.next.next = new Node(7);
console.log(`LinkedList cycle start: ${find_middle_of_linked_list(head).value}`); // 4
