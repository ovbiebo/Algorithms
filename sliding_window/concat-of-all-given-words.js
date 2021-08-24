// const find_word_concatenation = (s, words) => {
//     let result = [],
//         pattern = {},
//         matches = {},
//         wordLength = words[0].length,
//         front = wordLength * words.length,
//         back = 0;
//
//     for (const word of words) {
//         pattern[word] = (pattern[word] || 0) + 1;
//     }
//
//     while (front <= s.length) {
//         let i = front;
//         let word;
//
//         while (i > back) {
//             word = s.slice(i - wordLength, i)
//
//             if (pattern[word] && (matches[word] ?? 0) < pattern[word]) {
//                 matches[word] = (matches[word] ?? 0) + 1;
//                 i -= wordLength;
//             } else {
//                 matches = {}
//                 break;
//             }
//         }
//
//         if (i === back) {
//             matches = {};
//             result.push(i)
//         }
//
//         back++;
//         front++;
//     }
//
//     return result;
// };

const find_word_concatenation = (s, words) => {
    let result = [],
        pattern = {},
        wordLength = words[0].length;

    for (const word of words) {
        pattern[word] = (pattern[word] || 0) + 1;
    }

    for (let i = 0; i < wordLength; i++) {
        let back = i,
            front = back + wordLength,
            matches = {},
            count = 0

        while (front <= s.length) {
            let word = s.slice(front - wordLength, front);

            if (pattern[word]) {
                matches[word] = (matches[word] ?? 0) + 1;
                count++;

                while (matches[word] > pattern[word]) {
                    matches[s.slice(back, back + wordLength)] -= 1;
                    back += wordLength;
                    count--;
                }

                if (count === words.length) {
                    result.push(back)
                }
            } else {
                matches = {}
                count = 0;
                back = front;
            }

            front += wordLength;
        }
    }

    return result;
};

console.log(find_word_concatenation("a", ["a"])); // [0]
console.log(find_word_concatenation("foobarfoobarthefoobarman", ["foo", "bar"])); // [0,3,6,15]
console.log(find_word_concatenation("catfoxcat", ["cat", "fox"])); // [0, 3]
console.log(find_word_concatenation("catcatfoxfox", ["cat", "fox"])); // [3]
console.log(find_word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])); // []
console.log(find_word_concatenation("barfoothefoobarman", ["foo", "bar"])); // [0, 9]
console.log(find_word_concatenation("barfoofoobarthefoobarman", ["bar", "foo", "the"])); // [6,9,12]
console.log(find_word_concatenation("aaaaaaaaaaaaaa", ["aa", "aa"])); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(find_word_concatenation("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"])); // [13]
