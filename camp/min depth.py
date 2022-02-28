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
        
/////
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is not None:
            
            leftlen=self.minDepth(root.left)
        if root.right is not None:
            rightlen=self.minDepth(root.right)
        
        return min(leftlen,rightlen)+1
        
