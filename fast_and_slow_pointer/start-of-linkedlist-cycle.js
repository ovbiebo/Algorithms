class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }
}

const find_cycle_start = function (head) {
    let l = head;
    let r = head.next;
    let len = 0;

    while (l !== r) {
        r = r.next?.next;
        l = l.next;
    }

    do{
        l = l.next;
        len++;
    }while(l !== r)

    l = head;
    r = head;

    while(len > 0){
        r = r.next;
        len--;
    }

    while (l !== r) {
        r = r.next;
        l = l.next;
    }

    return l;
}

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);

head.next.next.next.next.next.next = head.next.next;
console.log(`LinkedList cycle start: ${find_cycle_start(head).value}`);

head.next.next.next.next.next.next = head.next.next.next;
console.log(`LinkedList cycle start: ${find_cycle_start(head).value}`);

head.next.next.next.next.next.next = head;
console.log(`LinkedList cycle start: ${find_cycle_start(head).value}`);
