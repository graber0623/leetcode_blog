# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        min_depth = 100000
        def dfs(node, d):
            nonlocal min_depth
            if not node:
                return
            d += 1
            print(".   ", d, min_depth, node.val, "    ")
            if not node.left and not node.right:
                min_depth = min(d, min_depth)
                return
            dfs(node.left, d)
            dfs(node.right, d)
        dfs(root, depth)
        return min_depth
