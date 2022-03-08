class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = [(root,1)]
        maxdepth=0
        
        
        while stack and root :
            node,depth=stack.pop()
                    
            if len(node.children)==0:
                maxdepth=max(maxdepth,depth)
            for i in node.children:                
                                              
                stack.append((i,depth+1))
            
                    
                    
                    
                
        return maxdepth
