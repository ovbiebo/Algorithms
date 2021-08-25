const find_missing_number = (nums) => {
    let missing_num = -1;

    let i = 0;
    while (i < nums.length) {
        let x = nums[i];
        if (x !== undefined && nums[x] !== nums[i]) {
            [nums[i], nums[x]] = [nums[x], nums[i]];
        } else {
            /* if the value at index i after swapping is
            undefined, then set missing number as i */
            if (x === undefined) missing_num = i;
            i++;
        }
    }

    return missing_num;
}

console.log(find_missing_number([4, 0, 3, 1]));
console.log(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]));
