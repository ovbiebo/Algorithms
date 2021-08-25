// const find_all_duplicates = (nums) => {
//     let i = 0;
//     while (i < nums.length) {
//         let x = nums[i] - 1;
//         if (nums[x] !== nums[i]) {
//             [nums[i], nums[x]] = [nums[x], nums[i]];
//         } else {
//             i++;
//         }
//     }
//
//     let duplicate_nums = [];
//     for (let i = 0; i < nums.length; i++) {
//         (i + 1 !== nums[i]) && duplicate_nums.push(nums[i]);
//     }
//
//     return duplicate_nums;
// }

const find_all_duplicates = (nums) => {
    let duplicate_nums = [];
    let i = 0;

    while (i < nums.length) {
        let x = nums[i] - 1;
        if (nums[x] !== nums[i]) {
            [nums[i], nums[x]] = [nums[x], nums[i]];
        } else {
            if (i !== x) duplicate_nums.push(x + 1);
            i++;
        }
    }

    return duplicate_nums;
}

console.log(`${find_all_duplicates([3, 4, 4, 5, 5])}`); // 4, 5
console.log(`${find_all_duplicates([5, 4, 7, 2, 3, 5, 3])}`); // 3, 5
