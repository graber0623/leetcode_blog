# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

#         if not root:
#             return False
            

#         if root.val == subRoot.val and root.left.val == subRoot.left.val and root.right.val == subRoot.right.val:
#             return True

#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

## ITS WRONG

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: ## I thought this was ok... hmmm

        def dfs(r, s):
            if not r and not s:
                return True
            elif not r or not s:
                return False
            elif r.val == s.val:
                s
                return dfs(r.left, s.left) and dfs(r.right, s.right)
            else:
                return dfs(r.left, s) or dfs(r.right, s)

        return dfs(root, subRoot) 

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(r, s):
            if not r and not s:
                return True
            elif not r or not s:
                return False
            return r.val == s.val and isSameTree(r.left, s.left) and isSameTree(r.right, s.right)

        def dfs(r, s):
            if not r:
                return False
            return isSameTree(r, s) or dfs(r.left, s) or dfs(r.right, s)

        return dfs(root, subRoot)
