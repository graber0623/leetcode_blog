# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        r1 = root
        r2 = root

        all_nodes = []

        def get_values_dfs(node):
            nonlocal all_nodes
            if not node:
                return
            all_nodes.append(node.val)

            get_values_dfs(node.left)
            get_values_dfs(node.right)

        get_values_dfs(r1)
        all_nodes = sorted(all_nodes)

        def sum_dfs(node):
            nonlocal all_nodes
            if not node:
                return
            node_val = node.val
            node.val += sum(all_nodes[all_nodes.index(node_val) +1 :])

            sum_dfs(node.left)
            sum_dfs(node.right)

        sum_dfs(r2)
        return r2
        