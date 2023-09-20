# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []

        def dfs(node):
            if not node.left and node.right:
                return_list.append(node.right.val)

            elif not node.right and node.left:
                return_list.append(node.left.val)
            
            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)
        
        dfs(root)

        return return_list

