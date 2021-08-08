const no_repeat_substring = (str) => {
    let result = 0;
    let loneChars = new Set();
    let length = 0;

    for (let i = 0; i < str.length; i++) {
        while (loneChars.has(str[i])){
            loneChars.delete(str[i - length--])
        }

        loneChars.add(str[i])
        length++

        result = Math.max(length, result);
    }

    return result;
};

console.log(no_repeat_substring("aabccbb")); // 3
console.log(no_repeat_substring("abbbb")); // 2
console.log(no_repeat_substring("abccde")); // 3
