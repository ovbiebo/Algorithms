const find_string_anagrams = (str, pattern) => {
    let result = []
    let counts = {}
    let patternCounts = {};
    let total = 0;

    for (const letter of pattern) {
        patternCounts[letter] = (patternCounts[letter] || 0) + 1
    }

    for (let i = 0; i < str.length; i++) {
        if (patternCounts[str[i]]) {
            counts[str[i]] = (counts[str[i]] || 0) + 1;
            total++;

            while (counts[str[i]] > patternCounts[str[i]]) {
                counts[str[i - --total]] -= 1;
            }
            if (total === pattern.length) result.push(i - (total - 1));
        }else{
            counts = {}
            total = 0;
        }
    }

    return result;
};

console.log(find_string_anagrams("ppqp", "pq")); // [1, 2]
console.log(find_string_anagrams("abbcabc", "abc")); // [2, 3, 4]
