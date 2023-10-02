# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#         r1 = root
#         lst = []
#         def all_val_dfs(node):
#             nonlocal lst
#             if not node:
#                 return
#             lst.append(node.val)
#             all_val_dfs(node.left)
#             all_val_dfs(node.right)
        
#         all_val_dfs(r1)

#         lst = sorted(lst)
#         mid = len(lst)-1//2
#         def tree_builder(mid,lst):
#             if mid <= 0 or mid >= len(lst):
#                 return
#             node = TreeNode(lst[mid])
#             node.left = tree_builder(mid//2,lst) 
#             node.right = tree_builder(mid+mid//2,lst)

#         return tree_builder(mid,lst)

class Solution:
    def balanceBST(self, root):
        
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ns = dfs(root)
        
        def build(l, r):
            if l > r: return None
            m = (l + r) // 2
            root = TreeNode(ns[m])
            root.left, root.right = build(l, m-1), build(m + 1, r)
            return root
        
        return build(0, len(ns) - 1)
