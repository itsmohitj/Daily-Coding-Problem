"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def PathSum(root: TreeNode):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val
        res = root.val
        res += min(PathSum(root.left), PathSum(root.right))
        return res

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.right = TreeNode(2)
    root.right = TreeNode(5)
    root.right.right = TreeNode(1)
    root.right.right.left = TreeNode(-1)
    print(PathSum(root))

# Time Complexity = O(n) where n is the number of nodes in the tree
# Space Complexity = O(n) 
