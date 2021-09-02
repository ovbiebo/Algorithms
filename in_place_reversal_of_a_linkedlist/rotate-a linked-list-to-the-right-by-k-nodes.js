class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }

    get_list() {
        let result = "";
        let temp = this;
        while (temp !== null) {
            result += temp.value + " ";
            temp = temp.next;
        }
        return result;
    }
}

const rotate = (head, k) => {
    if (!head || k < 1) return head;

    let r = head;
    let tail = r;

    let i = 0;
    while (head && r) {
        tail = r;
        r = r.next;
        i++
    }

    let newHead = i - k % i;
    let j = 0;
    r = head;
    while (j < newHead) {
        let _ = r;
        r = r.next;
        if (j + 1 === newHead) _.next = null;
        j++
    }

    tail.next = head;
    head = r;

    return head;
}

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);

console.log(`Nodes of the original LinkedList are: ${head.get_list()}`);
console.log(`Nodes of the rotated LinkedList are: ${rotate(head, 3).get_list()}`);
