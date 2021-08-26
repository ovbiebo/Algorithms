const find_corrupt_numbers = (nums) => {
    let corrupt_nums = [];

    let i = 0;
    while (i < nums.length) {
        let x = nums[i] - 1;
        if (nums[x] !== nums[i]) {
            [nums[i], nums[x]] = [nums[x], nums[i]];
        } else {
            i++;
        }
    }

    for (i = 0; i < nums.length; i++) {
        if (nums[i] !== i + 1) corrupt_nums.push(nums[i], i + 1);
    }

    return corrupt_nums;
}

console.log(`${find_corrupt_numbers([3, 1, 2, 5, 2])}`) // 2, 4
console.log(`${find_corrupt_numbers([3, 1, 2, 3, 6, 4])}`) // 3, 5
