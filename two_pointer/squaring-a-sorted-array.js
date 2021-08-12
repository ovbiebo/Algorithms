const make_squares = (arr) => {
    let result = [];

    let l = 0, r = arr.length - 1;

    while (l <= r) {
        const lSquare = arr[l] ** 2;
        if (l === r) {
            result.unshift(lSquare);
            break;
        }
        const rSquare = arr[r] ** 2;

        if (lSquare > rSquare) {
            result.unshift(lSquare);
            result.unshift(rSquare);
        } else {
            result.unshift(rSquare);
            result.unshift(lSquare);
        }
        r--;
        l++;
    }

    return result;
}

console.log(make_squares([-2, -1, 0, 2, 3])) // [0, 1, 4, 4, 9]
console.log(make_squares([-3, -1, 0, 1, 2])) // [0, 1, 1, 4, 9]
