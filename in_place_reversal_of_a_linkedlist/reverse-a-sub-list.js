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

const reverse_sub_list = (head, left, right) => {
    if (left >= right) return head;

    let l = null,
        r = head,
        i = 1;

    while (i < left) {
        l = r;
        r = r.next;
        i++;
    }

    let pNode = r;

    while (i <= right) {
        let _ = l;
        l = r;
        r = r.next;
        l.next = _;
        i++;
    }

    let _ = pNode.next
    pNode.next = r;
    (_) ?_.next = l : head = l;

    return head;
}

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);

console.log(`Nodes of the original LinkedList are: ${head.get_list()}`);
console.log(`Nodes of the reversed LinkedList are: ${reverse_sub_list(head, 2, 4).get_list()}`);
