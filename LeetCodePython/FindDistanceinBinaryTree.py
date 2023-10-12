# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        if p == q:
            return 0

        
        def max_parent(node):
            nonlocal p, q
            if not node:
                return
            
            if node.val == p or node.val == q:
                return node
            left = max_parent(node.left)
            right = max_parent(node.right)
            
            if left and right:
                return node
            if not left:
                return right
            else:
                return left

        
        mp = max_parent(root)

        s = []

        def finder(node, d):
            nonlocal p, q, s
            if not node:
                return
            
            if node.val == p or node.val == q:
                s.append(d)

            finder(node.left, d+1)
            finder(node.right, d+1)

        finder(mp, 0)

        return sum(s)