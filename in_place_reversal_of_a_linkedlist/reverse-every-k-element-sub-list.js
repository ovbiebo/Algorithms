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
* [1, 2, 3], k = 2
*
*
* l = null
* r = head
*
* while r exists
*   startNode = r
*   i = 0
    * while r exists and i < k
    *   let _ = l
    *   l = r
    *   r = r.next
    *   l.next = _
    *   i++;
    *
    * if(startNode.next) startNode.next.next = l else head = l
    * startNode.next = r
    * l = startNode
*
*/

const reverse_every_k_elements = (head, k) => {
    let l = null,
        r = head;

    while (r) {
        let startNode = r,
            i = 0;
        while (r && i < k) {
            let _ = l;
            l = r;
            r = r.next;
            l.next = _;
            i++;
        }
        
        (startNode.next)
            ? startNode.next.next = l
            : head = l;
        startNode.next = r;
        l = startNode
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
console.log(`Nodes of the reversed LinkedList are: ${reverse_every_k_elements(head, 3).get_list()}`);
