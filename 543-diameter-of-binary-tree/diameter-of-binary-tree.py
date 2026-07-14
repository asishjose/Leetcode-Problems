# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0, 0
            lh, ld = dfs(root.left)
            rh, rd = dfs(root.right)
            diameter = max(ld, rd, (lh+rh))
            height = 1 + max(lh, rh)
            return height, diameter
        return max(dfs(root.left)[1],
                   dfs(root.right)[1],
                   (dfs(root.right)[0]+dfs(root.left)[0]))