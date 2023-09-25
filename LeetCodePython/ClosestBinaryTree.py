# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_val = 1000000000


        def dfs(node):
            nonlocal min_val
            if not node:
                return
                
            if abs(node.val - target) < abs(min_val - target):
                min_val = node.val
            elif abs(node.val - target) == abs(min_val-target):
                min_val = min(min_val, node.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return min_val