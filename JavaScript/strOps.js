// Given a string, return a new string with the reversed order of character

function reverse(str) {
    let reverse = ""

    for (let char of str) {
        // appends "a" to the string reverse, then appends "b" and then "c"
        reverse = char + reverse
    }

    return reverse
};

function reverseInt(n) {
    let reverse = "";

    for (let char of n) {
        reverse = char + reverse
    }

    return parseInt(reverse)*Math.sign(n)

}

// Given a string, return true if it is a palindrome or false if it is not

function palindrome(str) {
    const reversed = str.split('').reverse().join('')
    return str === reversed
}

function maxChar(str) {
    const charMap = {}
    let max = 0
    let maxChar = ''

    for (let char of str) {
        if (charMap[char]) {
            charMap[char] = charMap[char]+=1
        } else{ 
            charMap[char] = 1
        }
    }

    for (let key in charMap) {
        if (charMap[key] > max) {
            max = charMap[key]
            maxChar = key
        }
    }

    return maxChar
}

console.log(maxChar("aaaabbbccccccccd"))

//console.log(reverse("abc"))
console.log(reverseInt("67"))

console.log(reverseInt("-67"))