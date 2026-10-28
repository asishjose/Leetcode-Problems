# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def isSameTree(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            if r1.val != r2.val:
                return False
            left = isSameTree(r1.left, r2.left)
            right = isSameTree(r1.right, r2.right)
            return left and right

        if subRoot is None:
            return True
        if root is None:
            return False
        if isSameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
