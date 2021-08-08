const smallest_subarray_with_given_sum = (s, arr) => {
    let result = 0;
    let sum = 0;
    let count = 0;

    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
        count++;
        while (sum >= s){
            result = result ? Math.min(count, result) : count;
            sum -= arr[i - --count] || 0;
        }
    }

    return result;
};

console.log(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])); // 2
console.log(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])); // 1
console.log(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])); // 3
