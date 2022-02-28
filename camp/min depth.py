class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth=1
        
        if not root:
            return 0
        
        def calc( root,depth):
            if not root :
                return float("inf")
            if root.left is None and root.right is None:
                return depth
            
            
            else:
                return min(calc(root.left,depth+1),calc(root.right,depth+1))
        return calc(root,depth)
        
