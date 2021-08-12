const remove_duplicates = (arr) => {
    let result = arr.length > 0 ? 1 : 0;

    let l = 0, r = 1;

    while (r < arr.length) {
        const diff = arr[r] - arr[l];
        (diff !== 0) && result++;
        r++;
        l++;
    }

    return result;
}

console.log(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) // 4
console.log(remove_duplicates([2, 2, 2, 11])) // 2
