const find_first_k_missing_positive = (nums, k) => {
    let i = 0;

    while (i < nums.length) {
        if(nums[i] < 1){
            i++;
            continue;
        }

        let x = nums[i] - 1;
        if (nums[x] !== nums[i]) {
            [nums[i], nums[x]] = [nums[x], nums[i]];
        } else {
            i++;
        }
    }

    let missing_nums = []
    i = 0;
    while (missing_nums.length < k) {
        if (nums[i] !== i + 1) missing_nums.push(i + 1);
        i++;
    }

    return missing_nums;
}

console.log(`${find_first_k_missing_positive([3, -1, 4, 5, 5], 3)}`) // [1, 2, 6]
console.log(`${find_first_k_missing_positive([2, 3, 4], 3)}`) // [1, 5, 6]
console.log(`${find_first_k_missing_positive([-2, -3, 4], 2)}`) // [1, 2]
