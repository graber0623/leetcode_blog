# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import defaultdict
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dic = defaultdict(list)
        def dfs(node, d):
            if not node:
                return
            d +=1
            if not node.left and not node.right:
                dic[d].append(node.val)
                return
            dfs(node.left, d)
            dfs(node.right, d)
        
        dfs(root, 0)
        dic = dict(sorted(dic.items(), reverse = True))
        deepest_level = max(dic.keys())
        return sum(dic[deepest_level])
