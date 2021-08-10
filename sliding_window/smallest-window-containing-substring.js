const find_substring = (str, pattern) => {
    let result = "",
        patternChars = {},
        startPt = 0,
        matches = {},
        matched = 0;

    for (const char of pattern) {
        patternChars[char] = (patternChars[char] || 0) + 1;
    }

    for (let i = 0; i < str.length; i++) {
        if (patternChars[str[i]]) {
            matches[str[i]] = (matches[str[i]] || 0) + 1;
            if (matches[str[i]] <= patternChars[str[i]]) matched++;
            if (matched === pattern.length) {
                while (!patternChars[str[startPt]] || matches[str[startPt]] - 1 >= patternChars[str[startPt]]) {
                    if (matches[str[startPt]]) matches[str[startPt]] -= 1;
                    startPt++;
                }

                const length = 1 + i - startPt;
                if (!result || length < result.length) result = str.substr(startPt, length);
            }
        }
    }

    return result;
};

console.log(find_substring("aabdec", "abc")); // "abdec"
console.log(find_substring("abdabca", "abc")); // "abc"
console.log(find_substring("adcad", "abc")); // ""
console.log(find_substring("aaaaaaaaaaaabbbbbcdd", "abcdd")); // "abbbbbcdd"
console.log(find_substring("ADOBECODEBANC", "ABC")); // "BANC"
