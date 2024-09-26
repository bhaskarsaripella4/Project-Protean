




input = "abcacbbdajkulellldellssb"

subString = ""

maxLen = 0
count = 0
for i in range(len(input)-1):
    for j in range(i,len(input)):
        subString = input[i:j]
        count += 1
        if (len(subString) == len(set(subString))):
            maxLen = max(len(subString), maxLen)
            print(subString)

        # if (len(subString) != len(set(subString))):
        #     break
        # maxLen = max(len(subString), maxLen)
        # print(subString)



print("number of bruteforce iterations:",count)
print("maxLen:",maxLen)


print("sliding window O(n) time complexity and O(n) memory complexity")
print("###################")
charSet = set()
left = 0
res = 0
count = 0
for right in range(len(input)):
    while input[right] in charSet:
        charSet.remove(input[left])
        left+=1
    charSet.add(input[right])
    res = max(res,right - left + 1)

print("maxLen:",res)
print("number of set sliding window iterations:",count)