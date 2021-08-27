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

const reverse = (head) => {
    let l = null;
    let r = head;

    while (r){
        // right side is evaluated first then the cached values are assigned to the left side
        [r, l, l.next] = [r.next, r, l];
    }
    head = l;

    return head;
}

head = new Node(2);
head.next = new Node(4);
head.next.next = new Node(6);
head.next.next.next = new Node(8);
head.next.next.next.next = new Node(10);

console.log(`Nodes of the original LinkedList are: ${head.get_list()}`);
console.log(`Nodes of the reversed LinkedList are: ${reverse(head).get_list()}`);
