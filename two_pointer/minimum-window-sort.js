const minimum_window_sort = (arr) => {
    let l = null;
    let smallest = null

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) {
            if (l === null) l = i;
            (smallest === null) ? smallest = arr[i] : smallest = Math.min(smallest, arr[i]);
        }
    }

    while(smallest < arr[l - 1]){
        l--;
    }

    let r = null;
    let largest = null

    for (let i = arr.length - 2; i >= 0; i--) {
        if (arr[i] > arr[i + 1]) {
            if (r === null) r = i + 1;
            (largest === null) ? largest = arr[i] : largest = Math.max(largest, arr[i]);
        }
    }

    while(largest > arr[r]){
        r++;
    }

    return (r - l) || 0;
}

console.log(minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12])) // 5
console.log(minimum_window_sort([1, 3, 2, 0, -1, 7, 10])) // 5
console.log(minimum_window_sort([1, 2, 3])) // 0
console.log(minimum_window_sort([3, 2, 1])) // 3
