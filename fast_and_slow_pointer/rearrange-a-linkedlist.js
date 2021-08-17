class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }

    print_list() {
        let result = '';
        let temp = this;
        while (temp !== null) {
            result += temp.value + " ";
            temp = temp.next;
        }
        console.log(result);
    }
}

const reorder = function (head) {
    let l = head;
    let r = head?.next;

    while (r) {
        r = r.next?.next;
        l = l.next;
    }

    r = l.next;
    l.next = null;

    while (r) {
        [l, r.next, r] = [r, l, r.next]
    }

    r = l;
    l = head;

    while (l.next !== r && l !== r) {
        [l.next, r.next, r, l] = [r, l.next, r.next, l.next];
    }

    return true;
}

head = new Node(2);
head.next = new Node(4);
head.next.next = new Node(6);
head.next.next.next = new Node(8);
head.next.next.next.next = new Node(10);
head.next.next.next.next.next = new Node(12);
reorder(head);
head.print_list();
