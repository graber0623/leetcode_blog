class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        def fn(node):
            """Return sum of nodes' value on sub-tree."""
            nonlocal ans
            if not node: return 0 
            sm = fn(node.left) + fn(node.right)
            if sm == node.val: ans += 1
            return sm + node.val 
        
        ans = 0 
        fn(root)
        return ans