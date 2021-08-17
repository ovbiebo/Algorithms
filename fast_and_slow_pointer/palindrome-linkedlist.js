class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }
}

const is_palindromic_linked_list = function (head) {
    let result = true;
    let l = head;
    let r = head.next || head;
    if (!r.next) return (r.value === l.value);

    let bl = {next: undefined};
    let isOdd = true;

    while (r) {
        if(!r.next) isOdd = false;
        r = r.next?.next;
        [bl, bl.next, l] = [l, bl, l.next];
    }

    (isOdd) ? r = l.next : r = l;

    while (bl && r) {
        if (bl.value !== r.value) result = false;
        [bl, l, l.next] = [bl.next, bl, l];
        r = r.next;
    }

    return result;
}

head = new Node(2);
head.next = new Node(4);
head.next.next = new Node(6);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(2);

console.log(`LinkedList cycle start: ${is_palindromic_linked_list(head)}`); // true
//
head.next.next.next.next.next = new Node(2);
console.log(`LinkedList cycle start: ${is_palindromic_linked_list(head)}`); // false
