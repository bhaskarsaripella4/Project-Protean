import math

arr = [100028,389798432,3891747332,32847193247]
# arr = [1,3,5,7]
threshold = 690890288
summation = math.inf
arrNew = [0]*len(arr)
divisor = 0

while summation >= threshold:
    divisor +=1
    summation = 0

    for i in range(len(arr)):

        arrNew[i] = math.ceil(arr[i]/pow(divisor,i))
        # print(arrNew[i])

    summation = sum(arrNew)

print(divisor)