const longest_substring_with_k_distinct = (str, k) => {
    let result = 0;
    let counts = new Map();
    let length = 0;

    for (let i = 0; i < str.length; i++) {
        counts.set(str[i], (counts.get(str[i]) || 0) + 1)
        length++;
        while (counts.size > k){
            const initial = str[i - --length]
            initial && counts.set(initial, (counts.get(initial)) - 1);
            !counts.get(initial) && counts.delete(initial)
        }
        result = Math.max(length, result);
    }

    return result;
};

console.log(longest_substring_with_k_distinct("araaci", 2)); // 4
console.log(longest_substring_with_k_distinct("araaci", 1)); // 2
console.log(longest_substring_with_k_distinct("cbbebi", 3)); // 5
