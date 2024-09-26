

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    maxSub = nums[0]
    currSub = 0

    for n in nums:
        if currSub < 0:
            currSub = 0
        currSub += n
        maxSub = max(maxSub,currSub)

    return maxSub

print(maxSubArray(nums))