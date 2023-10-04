# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## root.val = min(root.left.val, root.right.val)
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        first_min = root.val
        second_min = float('inf')

        def dfs(node):
            nonlocal first_min, second_min
            if not node: return
            
            if first_min < node.val and node.val < second_min:
                second_min = node.val
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if second_min == float('inf'):
            return -1
        return second_min
