# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        m = 100000
        def dfs(node):
            nonlocal m
            if not node:
                return
            
            if node.left and node.right:
                m = min(m, abs(node.val - node.left.val), abs(node.val - node.right.val))
            elif node.left and not node.right:
                m = min(m, abs(node.val - node.left.val))
            elif node.right and not node.left:
                m = min(m, abs(node.val - node.right.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return m