const search_triplets = (arr) => {
    let result = [];
    arr.sort((a, b) => a - b);

    for (let i = 0; i < arr.length; i++) {
        let l = i + 1;
        let r = arr.length - 1;
        let target = 0 - arr[i];

        while (l < r && arr[l] !== arr[l - 1]) {
            arr[l] + arr[r] === target && result.push([arr[i], arr[l], arr[r]]);
            (arr[l] + arr[r] > target) ? r-- : l++;
        }
    }

    return result;
}

console.log(search_triplets([-3, 0, 1, 2, -1, 1, -2])) // [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
console.log(search_triplets([-5, 2, -1, -2, 3])) // [[-5, 2, 3], [-2, -1, 3]]
