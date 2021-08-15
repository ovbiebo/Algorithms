const dutch_flag_sort = (arr) => {
    let l = 0;
    let r = arr.length - 1;

    let i = 0;
    while (i <= r) {
        if (arr[i] === 0) {
            [arr[i], arr[l]] = [arr[l], arr[i]];
            l++;
            i++;
        } else if (arr[i] === 1) {
            i++;
        } else {
            [arr[i], arr[r]] = [arr[r], arr[i]];
            r--;
        }
    }

    return arr;
}

console.log(dutch_flag_sort([1, 0, 2, 1, 0])) // [0 0 1 1 2]
console.log(dutch_flag_sort([2, 2, 0, 1, 2, 0])) // [0 0 1 2 2 2]
