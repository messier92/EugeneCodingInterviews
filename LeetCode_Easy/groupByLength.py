"""
"Given an array of strings, group them by their length. Return an object where the keys are the string lengths and the values are arrays of strings of that length."
"""

words = ["one", "two", "three", "four", "five", "six"]
res = {}

for i in range(len(words)):
    lengthOfWord = len(words[i])
    if lengthOfWord not in res:
        res[lengthOfWord] = [words[i]]
    else:
        res[lengthOfWord].append(words[i])
