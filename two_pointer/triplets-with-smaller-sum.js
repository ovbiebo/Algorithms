const triplet_with_smaller_sum = (arr, target_sum) => {
    let result = 0;
    arr.sort((a, b) => a - b);

    for (let i = 0; i < arr.length; i++) {
        let l = i + 1;
        let r = arr.length - 1;
        let target = target_sum - arr[i];

        while (l < r) {
            if (arr[l] + arr[r] >= target) {
                r--;
            } else {
                result += r - l;
                l++;
            }
        }
    }

    return result;
}

console.log(triplet_with_smaller_sum([-1, 0, 2, 3], 3)) // 2
console.log(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)) // 4
