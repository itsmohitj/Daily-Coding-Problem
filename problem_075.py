"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n
    lis = [1] * n
    for i in range(1,n):
        for j in range(0,i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j]+1)
    return max(lis)

# Time Complexity = O(n^2)
# Space Complexity = O(n)
