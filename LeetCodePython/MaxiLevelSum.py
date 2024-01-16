# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)        
        def dfs(node, depth):
            nonlocal d
            if not node:
                return
            
            depth += 1
            d[depth] += node.val
            dfs(node.left, depth)
            dfs(node.right, depth)
        
        dfs(root, 0)

        m = max(d.values())
        for key in sorted(d.keys()):
            if d[key] == m:
                break
        
        return key
