class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res  = []
        
        q=collections.deque()
        q.append(root)
        
        
        while q:
            qlen=len(q)
            level = []
            
            for i in range(qlen):
                node=q.popleft()
            
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(max(level))
                
        return res
                
