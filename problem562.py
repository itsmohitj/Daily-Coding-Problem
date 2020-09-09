"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# Using Division

def productOfAllButOne1(arr):
    prod = 1
    for i in arr:
        prod *= i
    for i in range(len(arr)):
        arr[i] = prod // arr[i]
    return arr

# Time Complexity = O(n)
# Space Complexity = O(1)

# Without Using Division

# 1. First Solution:
#--------------------------------------------------------------------------------------------------------------
# 1. Create two array prefix and suffix of length n, i.e length of the original array, initialize prefix[0] = 1 and suffix[n-1] = 1 and also another array to store the product.
# 2. Traverse the prefix array from second index to end and for every index i update prefix[i] as prefix[i] = prefix[i-1] * array[i-1], i.e store the product till i-1 index from the start of array.
# 3. Traverse the suffix array from second last index to start and for every index i update suffix[i] as suffix[i] = suffix[i+1] * array[i+1], i.e store the product till i+1 index from the end of array.
# 4. For every index i, update arr[i] = prefix[i] * suffix[i].

def productOfAllButOne2(arr):
    n = len(arr)
    if n == 1:
        return 0
    prefix = [0 for i in range(n)]
    suffix = [0 for i in range(n)]
    prefix[0] = 1
    suffix [n-1] = 1
    
    for i in range(1,n):
        prefix[i] = prefix[i-1] * arr[i-1]

    for j in range(n-2,-1,-1):
        suffix[j] = suffix[j+1] * arr[j+1]

    for i in range(n):
        arr[i] = prefix[i] * suffix[i]

    return arr

# Time Complexity = O(n)
# Space Complexity = O(n)

#--------------------------------------------------------------------------------------------------------------------------
# 2. Log Based Solution:
#--------------------------------------------------------------------------------------------------------------------------------
"""
Using the following property of log:
x = a * b * c * d
log(x) = log(a * b * c * d)
log(x) = log(a) + log(b) + log(c) + log(d)
x = antilog(log(a) + log(b) + log(c) + log(d))

Now, if we have to remove ith element from the product it will be:
    x = antilog(log(a[0]) + log(a[1]) +.....+ log(a[n-1]) + log(a[n]) - log(a[i]))

"""
import math

def productOfAllButOne3(arr):
    sum = 0
    n=len(arr)
    for i in range(n):
        sum += math.log10(arr[i])
    
    for i in range(n):
        arr[i] = math.ceil(pow(10.00,sum-math.log10(arr[i])))

    return arr

# Time Complexity = O(n)
# Space Complexity = O(1)



if __name__ == '__main__':
    arr1 = [1,2,3,4,5]
    arr2 = [3,2,1]
    print(productOfAllButOne3(arr1))
    print(productOfAllButOne2(arr2))

