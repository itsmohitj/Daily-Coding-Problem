"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]

if __name__ == '__main__':
    arr = [1,2,1,1,3,4,0]
    print(majorityElement(arr))
