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

/*
* [1, 2], k = 1
* [1, 2, 3, 4], k = 4
* [1, 2, 3, 4, 5], k = 3
* [1, 2, 3], k = 2
*/

const reverse_alternate_k_elements = (head, k) => {
    let l = null;
    let r = head;

    while (r) {
        let i = 0;
        let pNode = r;
        while (r && i < k) {
            let _ = l;
            l = r;
            r = r.next;
            l.next = _;
            i++;
        }
        (pNode.next) ? pNode.next.next = l : head = l;
        pNode.next = r

        i = 0;
        while (r && i < k) {
            l = r;
            r = r.next;
            i++
        }
    }

    return head;
}

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);
head.next.next.next.next.next.next = new Node(7);
head.next.next.next.next.next.next.next = new Node(8);

console.log(`Nodes of the original LinkedList are: ${head.get_list()}`);
console.log(`Nodes of the reversed LinkedList are: ${reverse_alternate_k_elements(head, 2).get_list()}`);
