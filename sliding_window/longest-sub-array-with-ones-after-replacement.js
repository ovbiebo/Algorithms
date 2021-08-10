const length_of_longest_subarray = (arr, k) => {
    let result = 0;
    let counts = {};
    let length = 0;

    for (let i = 0; i < arr.length; i++) {
        counts[arr[i]] = (counts[arr[i]] || 0) + 1;
        length++;

        while (length > counts[1] + k) {
            counts[arr[i - --length]] -= 1;
        }
        result = Math.max(length, result);
    }

    return result;
};

console.log(length_of_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)); // 6
console.log(length_of_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)); // 9
