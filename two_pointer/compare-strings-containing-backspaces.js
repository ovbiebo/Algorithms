const backspace_compare = (str1, str2) => {
    let l = str1.length - 1;
    let r = str2.length - 1;

    while (l >= 0 && r >= 0) {
        let bl = 0;
        while (str1[l] === '#') {
            bl++
            l--;
        }

        l -= bl;
        bl = 0;

        let br = 0;
        while (str2[r] === '#') {
            br++
            r--;
        }

        r -= br;
        br = 0;

        if (str1[l] !== str2[r]) return false;
        r--;
        l--;
    }

    return true;
}

console.log(backspace_compare("xy#z", "xzz#")) // true
console.log(backspace_compare("xy#z", "xyz#")) // false
console.log(backspace_compare("xp#", "xyz##")) // true
console.log(backspace_compare("xywrrmp", "xywrrmu#p")) // true
