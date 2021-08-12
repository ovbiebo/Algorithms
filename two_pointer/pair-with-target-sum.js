const pair_with_targetsum = (arr, target_sum) => {
    let result = [];

    let l = 0, r = arr.length - 1;

    while (l < r) {
        const sum = arr[l] + arr[r]
        if (sum === target_sum) {
            result = [l, r];
            break;
        }
        if (sum > target_sum) r--;
        if (sum < target_sum) l++;
    }

    return result;
}

console.log(pair_with_targetsum([1, 2, 3, 4, 6], 6)) // [1, 3]
console.log(pair_with_targetsum([2, 5, 9, 11], 11)) // [0, 2]
