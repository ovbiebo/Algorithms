const find_permutation = (str, pattern) => {
    let counts = {}
    let patternCounts = {};
    let total = 0;
    pattern = [...pattern]

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
            if (total === pattern.length) return true;
        }else{
            counts = {}
            total = 0;
        }
    }

    return false;
};

console.log(find_permutation("oidbcaf", "abc")); // true
console.log(find_permutation("odicf", "dc")); // false
console.log(find_permutation("bcdxabcdy", "bcdyabcdx")); // true
console.log(find_permutation("aaacb", "abc")); // true
