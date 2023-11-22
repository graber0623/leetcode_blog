# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        def dfs(node, lastval, last_dir):
            nonlocal ans
            if not node:
                return
            
            if last_dir == 'l' and node.val >= lastval:
                ans = False
                return
            
            if last_dir == 'r' and node.val <= lastval:
                ans = False
                return
            
            lv = node.val
            dfs(node.left, lv, 'l')
            dfs(node.right, lv, 'r')
        dfs(root, 0, 'a')

        return ans
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        def dfs(node, min_val, max_val):
            nonlocal ans
            if not node:
                return
            
            if not min_val < node.val < max_val:
                ans = False
                return

            changer = node.val

            dfs(node.left, min_val, changer)
            dfs(node.right, changer, max_val)

        dfs(root, float('-inf'), float('inf'))

        return ans