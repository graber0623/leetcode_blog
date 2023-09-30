# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = 0
        def dfs(node, p):
            nonlocal s

            if not node:
                return

            if len(p) >= 2 and p[-2] % 2 == 0:
                s += node.val

            p.append(node.val)
            dfs(node.left, p.copy())
            dfs(node.right, p.copy())

        dfs(root, [])

        return s
            

