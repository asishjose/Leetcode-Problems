# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return True, 0
            lb, lh = dfs(root.left)
            rb, rh = dfs(root.right)
            height = 1 + max(lh, rh)
            balanced = abs(lh-rh) <= 1 and lb and rb
            return balanced, height
        return dfs(root)[0]
        