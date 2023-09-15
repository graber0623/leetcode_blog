# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        a = []

        def dfs(node):
            nonlocal a
            if not node:
                return
            a.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        if len(set(a)) == 1:
            return True
        else:
            return False
## could have returned false when val doesnt match last one.. 