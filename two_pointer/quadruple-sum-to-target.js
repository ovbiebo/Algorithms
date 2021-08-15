const search_quadruplets = (arr, target) => {
    let result = [];
    arr.sort((a, b) => a - b);

    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            let l = j + 1;
            let r = arr.length - 1;
            let rem_sum = target - arr[j] - arr[i];

            while (l < r && (arr[l] !== arr[l - 1] || (l - 1) === j)) {
                arr[l] + arr[r] === rem_sum && result.push([arr[i], arr[j], arr[l], arr[r]]);
                (arr[l] + arr[r] > rem_sum) ? r-- : l++;
            }
        }
    }

    return result;
}

console.log(search_quadruplets([4, 1, 2, -1, 1, -3], 1)) // [-3, -1, 1, 4], [-3, 1, 1, 2]]
console.log(search_quadruplets([2, 0, -1, 1, -2, 2], 2)) // [[-2, 0, 2, 2], [-1, 0, 1, 2]]
