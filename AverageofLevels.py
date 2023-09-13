from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr = defaultdict(list)
        def dfs(node, depth):
            if not node:
                return
            
            if not arr[depth]:
                arr[depth] = [node.val, 1]
            else:
                arr[depth][0] += node.val
                arr[depth][1] += 1
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)
        print(arr)
        return [value[0]/value[1] for value in list(arr.values())]
            