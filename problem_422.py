"""
This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1

# Time complexity : O(n). A total of n nodes need to be traversed. Here, n represents the minimum number of nodes from the two given trees.

# Space complexity : O(n). The depth of the recursion tree can go upto n in the case of a skewed tree. In average case, depth will be O(logn).
