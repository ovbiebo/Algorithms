const max_sub_array_of_size_k = (k, arr) => {
    let result = 0;
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
        sum += arr[i] - (arr[i - k] || 0)
        result = Math.max(sum, result)
    }

    return result;
}	

console.log(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]));// 9
console.log(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])); // 7