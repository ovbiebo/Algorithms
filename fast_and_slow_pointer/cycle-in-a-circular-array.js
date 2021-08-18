const circular_array_loop_exists = (arr) => {
    let l = 0,
        r = 0;

    do {
        l = move(arr, l);
        r = move(arr, r);
        r = move(arr, r);
    } while (l !== r)

    let len = 0;
    let dir = 0;
    do {
        if (Math.abs(dir) > Math.abs(dir += arr[l])) return false;
        l = move(arr, l);
        len++;
    } while (l !== r)

    return (len < arr.length && len > 1);
}

const move = (arr, i) => {
    i += arr[i];
    (i < 0) ? i = arr.length + i : i = i % arr.length;
    return i;
}

console.log(circular_array_loop_exists([1, 2, -1, 2, 2])) // true
console.log(circular_array_loop_exists([2, 2, -1, 2])) // true
console.log(circular_array_loop_exists([2, 1, -1, -2])) // false
