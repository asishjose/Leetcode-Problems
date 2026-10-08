# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def height(root):
            nonlocal maxDiameter
            if root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            curr_diameter = lh+rh
            maxDiameter = max(maxDiameter, curr_diameter)
            return 1 + max(lh, rh)
        height(root)
        return maxDiameter