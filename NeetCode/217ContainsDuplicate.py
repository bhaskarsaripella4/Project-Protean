

# nums = [1,1,1,3,3,4,3,2,4,2]
# nums = [1,2,3,4]
nums = [1,2,3,4,2]

# def containsDuplicate(nums):
#     distinct_nums = set()
#
#     for x in nums:
#         if (x in distinct_nums):
#             return True
#             break
#         else:
#             distinct_nums.add(x)
#     return False
#
#
# print(containsDuplicate(nums))


def containsDuplicate2(nums):
    unique = set()

    for num in nums:
        if(num in unique):
            return True
        unique.add(num)
    return False

print(containsDuplicate2(nums))