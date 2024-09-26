
# nums = [2 ,7 ,9 ,3 ,1]
# nums = [1 ,2 ,3 ,1]
# nums = [2,9,7,1,3,6,8]
# nums = [1,2]
# nums = [1]

nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]

#this fails for edge cases and takes a long time too. Didn't even reach 70 test cases yet.
# numPosibilities = round(len(nums)/2)
#
# maxSum = 0
# if(numPosibilities == 0):
#     maxSum = nums[0]
#
# for i in range(numPosibilities):
#     sum = 0
#     j = i
#     if(len(nums[i:])==1):
#         sum = sum+nums[i+1]
#     while(j < len(nums[i:])):
#         sum = sum+nums[j]
#         j+=2
#     if(maxSum<sum):
#         maxSum = sum
l_sum,r_sum = 0,0

# this solution fails for large arrays as the tree becomes huge. time limit exceeded
def findPossibleHomes(arr):
    if(len(arr) <= 2):
        return max(arr)
    return max(arr[0] + findPossibleHomes(arr[2:]),
               findPossibleHomes(arr[1:]))

# print(findPossibleHomes(nums))


def robber(arr):
    rob1, rob2 = 0, 0
    for n in arr:
        temp = max(n+rob1,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(robber(nums))