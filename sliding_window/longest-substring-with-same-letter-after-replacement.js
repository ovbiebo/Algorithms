const length_of_longest_substring = (str, k) => {
    let result = 0;
    let counts = {};
    let length = 0;
    let highestCharFreq = 1;

    for (let i = 0; i < str.length; i++) {
        counts[str[i]] = (counts[str[i]] || 0) + 1;
        highestCharFreq = Math.max(counts[str[i]], highestCharFreq);
        length++;

        while (length > highestCharFreq + k) {
            counts[str[i - --length]] -= 1;
        }
        result = Math.max(length, result);
    }

    return result;
};

console.log(length_of_longest_substring("aabccbb", 2)); // 5
console.log(length_of_longest_substring("abbcb", 1)); // 4
console.log(length_of_longest_substring("abccde", 1)); // 3
