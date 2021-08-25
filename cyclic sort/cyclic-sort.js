const cyclic_sort = (nums) => {
    let i = 0;
    while (i < nums.length) {
        let x = nums[i];
        [nums[i], nums[x - 1]] = [nums[x - 1], x];
        if (i === x - 1) i++;
    }

    return nums;
}

console.log(`${cyclic_sort([3, 1, 5, 4, 2])}`)
console.log(`${cyclic_sort([2, 6, 4, 3, 1, 5])}`)
console.log(`${cyclic_sort([1, 5, 6, 4, 3, 2])}`)
