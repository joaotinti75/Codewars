/* Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces. */

function getCount(str) {
    let vowelsCount = 0;
    let vowels = ['a','e','i','o','u']
    str = [...str]
    str.forEach((el) => {
        if (vowels.indexOf(el) >= 0) {
            vowelsCount++
        }
    })
        
    return vowelsCount;
}

