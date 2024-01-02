# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0
        def dfs(node, premax):
            nonlocal c
            if not node:
                return
            if node.val >= premax:
                c+=1
            premax = max(premax, node.val)
            dfs(node.left, premax)
            dfs(node.right, premax)

        dfs(root, root.val)
        return c
