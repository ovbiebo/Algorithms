const find_first_missing_positive = (nums) => {
    let i = 0;

    while (i < nums.length) {
        if(nums[i] < 1 || nums[i] > nums.length){
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

    for (i = 0; i < nums.length; i++) {
        if (nums[i] !== i + 1) return i + 1;
    }

    return nums[nums.length - 1] + 1;
}

console.log(`${find_first_missing_positive([-3, 1, 5, 4, 2])}`) // 3
console.log(`${find_first_missing_positive([3, -2, 0, 1, 2])}`) // 4
console.log(`${find_first_missing_positive([3, 2, 5, 1])}`) // 4
