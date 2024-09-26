

nums = [-1,3,-8,4]

def maxProductSubArr(nums):

    maxProd = nums[0]
    curProd = 1

    for n in nums:
        if curProd < maxProd:
            currProd = maxProd
        curProd *= n
        maxProd = max(maxProd,curProd)

    return maxProd


    return 0



print(maxProductSubArr(nums))