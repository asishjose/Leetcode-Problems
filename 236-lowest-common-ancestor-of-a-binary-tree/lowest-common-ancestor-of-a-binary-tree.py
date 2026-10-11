# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []

        self.findPath(root, p, path1)
        self.findPath(root, q, path2)

        ans = None
        pathLen = min(len(path1), len(path2))
        i = 0
        while i < pathLen and path1[i] is path2[i]:
            ans = path1[i]
            i+=1

        return ans

    def findPath(self, root, value, path):
        if root is None:
            return False
        
        path.append(root)

        if root.val == value.val:
            return True

        if self.findPath(root.left, value, path) or self.findPath(root.right, value, path):
            return True

        path.pop()
        return False