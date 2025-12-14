function charMap(str) {
    const charMap = {}

    str = str.toLowerCase().replace(/[\W]/g,'')
    for (let char of str) {
        // shorthand to increment value in dictionary otherwise init as 1
        charMap[char] = ++charMap[char] || 1
    }

    console.log(charMap)

    return charMap
}

function anagrams(stringA, stringB) {
    const charMapA = charMap(stringA)
    const charMapB = charMap(stringB)
    // check length
    if (Object.keys(charMapA).length != Object.keys(charMapB).length)
        return false
    // check char
    for (let key in charMapA) {
        if (charMapA[key]!==charMapB[key]) {
            return false
        }
    }
    return true
}

console.log(anagrams("abc","cba"))