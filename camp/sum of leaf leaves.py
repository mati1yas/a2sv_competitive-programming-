class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.tot = 0
        
        def dfs (root):
            if not root:
                return 0
            if root.left and not root.left.left and not root.left.right:
                self.tot += root.left.val
            dfs(root.left)
            dfs(root.right)
            return 
            
            
            
        
        dfs(root)
        return self.tot
