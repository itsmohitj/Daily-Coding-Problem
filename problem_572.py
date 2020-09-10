"""
This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""

def nextPermutation(nums):
        n = len(nums)
        pivot, right = n - 2, n - 1

        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -= 1

        if pivot == -1:
            nums.reverse()
            return

        while right > pivot and nums[right] <= nums[pivot]:
            right -= 1
        nums[pivot], nums[right] = nums[right], nums[pivot]
        nums[pivot+1:] = nums[pivot+1:][::-1]
        return nums

if __name__ == '__main__':
    arr = [1,3,5,4,2]
    print(nextPermutation(arr))
