const find_duplicate = (nums) => {
    let i = 0;
    while (i < nums.length) {
        let x = nums[i] - 1;
        if (nums[x] !== nums[i]) {
            [nums[i], nums[x]] = [nums[x], nums[i]];
        } else {
            if(i === nums[i]) return i;
            i++;
        }
    }
}

console.log(find_duplicate([1, 4, 4, 3, 2])); // 4
console.log(find_duplicate([2, 1, 3, 3, 5, 4])); // 3
console.log(find_duplicate([2, 4, 1, 4, 4])); // 4
