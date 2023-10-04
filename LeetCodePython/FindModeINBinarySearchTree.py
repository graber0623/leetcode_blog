from collections import defaultdict

d = defaultdict(list)

d[1] = [1,2,3,4]
d[3] = [1,2,3]
print(list(d.keys()))
# d_items = sorted(d.items(), reverse = True)

# print(list(d_items[0])[1])


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# from collections import defaultdict
# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         d = defaultdict(list)
#         count = 0
#         last_value = 100001
#         def dfs(node, c, last_val):
#             if not node: return
#             c += 1
#             if last_val != node.val:
#                 d[c].append(last_val)
#                 dfs(node.left, 0, node.val)
#                 dfs(node.right, 0, node.val)
#             else:
#                 dfs(node.left, c, node.val)
#                 dfs(node.right, c, node.val)
#         dfs(root, count, last_value)
#         print(d)
#         d_items = sorted(d.items(), reverse = True)
#         return list(d_items[0])[1]

## WRONG SOLUTION