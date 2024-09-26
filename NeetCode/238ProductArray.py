
import numpy as np

nums = [1,2,3,4]

soln = {}

# def ProductExclSelf(nums):
#
#     for i,num in enumerate(nums):
#         prod = 1
#         for j,n in enumerate(nums):
#             prod = prod*n
#         soln[i] = (int) (prod/num) # repeat without division operator
#
#     return soln
#
# print(ProductExclSelf(nums))

hash = {}

def ProductExclSelf(nums):

    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix*nums[i]

    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix = postfix*nums[i]
    return res
print(ProductExclSelf(nums))
