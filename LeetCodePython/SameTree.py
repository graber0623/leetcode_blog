# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(f,s):
            if not f and s:
                return False
            if f and not s:
                return False  
            if not f and not s:
                return True
            else:
                if f.val != s.val:
                    return False
                else:
                    return dfs(f.left, s.left) and dfs(f.right, s.right)
        return dfs(p,q)

