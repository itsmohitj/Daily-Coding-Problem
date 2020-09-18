"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
"""

def firstMissingPositive(self, nums: List[int]) -> int:
    if not nums:
        return 1
    for i in range(1,abs(max(nums))+2):
        if i not in nums:
            return i

# Time Complexity = O(n)
# Space Complexity = O(1)
