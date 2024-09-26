




nums = [2,1,5,3]
target = 4

def twoSum(nums,target):
    prevMap = {} # hashmap stores value vs index. if diff is a value in the hashmap, return the index from the hashmap.
    for i,num in enumerate(nums):
        diff = target-num
        if(diff in prevMap):
            return [prevMap[diff],i]
        prevMap[num] = i

print(twoSum(nums,target))