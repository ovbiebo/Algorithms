const triplet_sum_close_to_target = (arr, target_sum) => {
    let result = null;
    arr.sort((a, b) => a - b);

    for (let i = 0; i < arr.length; i++) {
        let l = i + 1;
        let r = arr.length - 1;
        let target = target_sum - arr[i];

        while (l < r) {
            const sum = arr[i] + arr[l] + arr[r];
            if (result === null || Math.abs(target_sum - result) > Math.abs(target_sum - sum)) {
                result = sum;
            }
            (arr[l] + arr[r] > target) ? r-- : l++;
        }
    }

    return result;
}

console.log(triplet_sum_close_to_target([-2, 0, 1, 2], 2)) // 1
console.log(triplet_sum_close_to_target([-3, -1, 1, 2], 1)) // 0
console.log(triplet_sum_close_to_target([1, 0, 1, 1], 100)) // 3
