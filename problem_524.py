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
