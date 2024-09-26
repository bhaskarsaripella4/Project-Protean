









input = "ABAB"
# input = "ABBBAAB"

k = 1  #number of replacements possible
left = 0
hashMap = {}
res = 0
count = 0

for right in range(len(input)):
    hashMap[input[right]] = 1 + hashMap.get(input[right], 0)
    while (right - left  +1) - max(hashMap.values()) > k :
        hashMap[input[left]] -= 1
        left += 1


        res = max(res, right - left + 1)


print("max replaceable substring lenght:",res)


## without changing maxFrequency of characters
for right in range(len(input)):
    