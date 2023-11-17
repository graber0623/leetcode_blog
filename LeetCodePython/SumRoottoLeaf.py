# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(n_str, node):
            nonlocal ans
            if not node:
                return
            n_str += str(node.val)
            if not node.left and not node.right:
                ans+=(int(n_str))
                return
        
            dfs(n_str, node.left)
            dfs(n_str, node.right)
        
        dfs('', root)

        return ans
            
