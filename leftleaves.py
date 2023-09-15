# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        l = []
        def dfs(node, hand):
            if not node:
                return

            if not node.left and not node.right and hand == "left":
                l.append(node.val)
            
            hand = "right"
            dfs(node.right, hand)
            hand = "left"
            dfs(node.left, hand)
        dfs(root, "root")
        return sum(l)