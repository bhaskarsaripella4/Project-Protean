
def findDup(s):

    charMap = {}

    for string in s:
        for char in string:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1

    return charMap


# filter for duplicates
result = findDup("This is interview Prep")
dup = {char: count for char,count in result.items() if count > 1}
print(dup)
