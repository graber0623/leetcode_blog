# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root: return True
    
#         def dfs(node):
#             if not node:
#                 return 0
#             l = dfs(node.left)
#             r = dfs(node.right)

#             if l < 0 or r < 0 or abs(l-r)>1:
#                 return -1
             
#             return max(l, r)+1
        

#         return dfs(root) >= 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node): ## return bool / height
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1


            return [balanced, 1+max(left[1], right[1])]
        
        return dfs(root)[0]


