const find_happy_number = (num) => {
    let l = find_square_sum(num);
    let r = find_square_sum(l);

    while (l !== r){
        if (l === 1 || r === 1) return true
        l = find_square_sum(l);
        r = find_square_sum(find_square_sum(r))
    }

    return false;
}

const find_square_sum = (num) => {
    let sum = 0;
    while (num > 0) {
        let digit = num % 10;
        sum += digit ** 2;
        num = Math.floor(num / 10);
    }
    return sum;
}

console.log(`${find_happy_number(23)}`) // true
console.log(`${find_happy_number(12)}`) // false
