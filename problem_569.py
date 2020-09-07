#This problem was asked by Facebook.

#Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.

# 1. Linear Method:
#------------------------------------------------------------------
# 1. Check the length of the array. If length is 1, then maximum and minimum will be the only element of the array.
# 2. If value is greater than 1, Initialize value of max and min as maximum and minimum of first two elements of array respectively.
# 3. Starting from 3rd, compare each element with max and min, and change max and min accordingly


def getMinMax1(arr):
    n=len(arr)
    if n == 1:
        mx = mn = arr[0]

    if arr[0]>arr[1]:
        mx=arr[0]
        mn=arr[1]
    else:
        mx=arr[1]
        mn=arr[0]

    for i in range(2,n):
        if arr[i] > mx:
            mx = arr[i]
        elif arr[i] < mn:
            mn = arr[i]
    return mx,mn

# Time Complexity = O(n)
# Space Complexity = O(1)
# Comparisons = 1 + 2(n-2) in worst case and 1+ (n-2) in best case
#---------------------------------------------------------------------------------

# 2. Pair Comparison:
#-----------------------------------------------------------------------------------

# 1. Check the length of the array. If it is odd, then initialize min and max to first element of the array and start variable to 1. Start variable indicates the start value to loop through the array.
# 2. If length of the array is even, then initialize min and max as min and max of first two elements of array respectively.
# 3. Starting from the start variable, find the max and min between ith and (i+1)th element. Then compare with current min and max and change accordingly and jump over 2 steps in loop.

def getMinMax2(arr):
    n=len(arr)
    if n % 2 == 0:
        mn = min(arr[0],arr[1])
        mx = max(arr[0],arr[1])
        start = 2
    else:
        mn = mx = arr[0]
        start = 1

    for i in range(start, n ,2):
        if max(arr[i],arr[i+1]) > mx :
            mx = max(arr[i],arr[i+1])
        elif min(arr[i],arr[i+1]) < mn:
            mn = min(arr[i],arr[i+1])
    return mx,mn

if __name__ == '__main__':
    arr = [123,436,54,744,983,844,283,4482,22,543,9,874]
    mx1, mn1 = getMinMax1(arr)
    mx2, mn2 = getMinMax2(arr)
    print(mx1,mx2,mn1,mn2)i

# Time Complexity = O(n)
# Space Complexity = O(1)
# Comparisons :
#   If n is odd = 1+3(n-2)/2 = 3n/2
#   If n is even = 3+3(n-2)/2 = (3n+4)/2
