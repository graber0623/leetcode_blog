# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(node, p):
            nonlocal ans
            if not node:
                return
            if p == '':
                p += str(node.val)
            else:
                p += '->'+str(node.val)

            if not node.left and not node.right:
                ans.append(p)
                return
            
            dfs(node.left, p)
            dfs(node.right, p)

        dfs(root, str(''))

        return ans
        