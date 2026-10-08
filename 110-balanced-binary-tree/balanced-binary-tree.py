# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        bal = True
        def height(root):
            nonlocal bal
            if root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            bal = bal and abs(lh-rh)<2
            return 1 + max(lh, rh)
        height(root)
        return bal