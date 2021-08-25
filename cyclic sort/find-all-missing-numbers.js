const find_missing_numbers = (nums) => {
    let i = 0;
    while (i < nums.length) {
        let x = nums[i] - 1;
        if (nums[x] !== nums[i]) {
            [nums[i], nums[x]] = [nums[x], nums[i]];
        } else {
            i++;
        }
    }

    let missing_nums = [];
    for (i = 1; i <= nums.length; i++) {
        (i !== nums[i - 1]) && missing_nums.push(i)
    }

    return missing_nums;
}

console.log(`${find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1])}`); // 4, 6, 7
console.log(`${find_missing_numbers([2, 4, 1, 2])}`); // 3
console.log(`${find_missing_numbers([2, 3, 2, 1])}`); // 4
