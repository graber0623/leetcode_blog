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
    
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        m = []
        def dfs(node):
            nonlocal m
            if not node:
                return
            m.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        min_val = 100000
        for i in range(len(m)):
            for j in range(i+1, len(m)):
                min_val = min(min_val, abs(m[i]-m[j]))



        return min_val
    ## DONT FORGET THAT IT IS A BINARY SEARCH TREE!!!! SEARCH TREE!!!!!