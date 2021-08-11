const find_word_concatenation = (str, words) => {
    let result = [],
        matches = {},
        pattern = {},
        total = 0,
        wordLength = words[0].length,
        r = wordLength;

    for (const word of words) {
        pattern[word] = (pattern[word] || 0) + 1;
    }

    while (r <= str.length) {
        let word = str.slice(r - wordLength, r)
        if (pattern[word]) {
            matches[word] = (matches[word] || 0) + 1;
            total++;

            while (matches[word] > pattern[word]) {
                let k = str.slice(r - total * wordLength, r - --total * wordLength);
                matches[k] -= 1;
            }

            if (total === words.length) {
                result.push(r - total * wordLength);
            }
            r += wordLength;
        } else {
            matches = {};
            total = 0;
            r++;
        }
    }

    return result;
};

console.log(find_word_concatenation("catfoxcat", ["cat", "fox"])); // [0, 3]
console.log(find_word_concatenation("catcatfoxfox", ["cat", "fox"])); // [3]
console.log(find_word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])); // []
console.log(find_word_concatenation("barfoofoobarthefoobarman", ["bar", "foo", "the"])); // [6,9,12]
