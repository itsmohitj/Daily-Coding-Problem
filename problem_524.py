"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

def maxSubarraySum(arr,size):
    overallMax = 0
    maxTillNow = 0
    for i in range(size):
        maxTillNow = maxTillNow+arr[i]
        if(maxTillNow < 0):
            maxTillNow = 0
        elif(overallMax < maxTillNow):
            overallMax = maxTillNow
    return overallMax

arr1=[34,-50,42,14,-5,86]
arr2=[-5,-1,-8,-9]
print(maxSubarraySum(arr1,6))
print(maxSubarraySum(arr2,4))

# Time Complexity = O(n)
# Space Complexity = O(1)
