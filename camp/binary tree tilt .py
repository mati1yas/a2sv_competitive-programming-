class Solution:
    
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.tilt=0
        def dfs(root):
            
            if not root:
                return 0
            
        
            left=dfs(root.left)
            right=dfs(root.right)
            self.tilt+=abs(right-left)
            
            return left + right + root.val
        dfs(root)
        return self.tilt
        
