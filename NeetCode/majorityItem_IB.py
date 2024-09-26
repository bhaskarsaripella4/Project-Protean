import math


def majorityElement(A):
    threshold = math.floor(len(A) /2)

    map = {}

    for item in A:
        if item in map:
             map.update({item :map.get(item)+1})

        else:
            map.update({item :1})
    print(map.items())
    majority = ([x for x, c in map.items() if c > threshold])
    if majority:
        return majority[0]
    else:
        return None




A = [2, 1, 2,3,5,2,1]
A = [2, 1, 2]
print(majorityElement(A))