class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        sd=[(dist[i],speed[i]) for i in range(len(dist))]
        sd.sort(key= lambda x:x[0]/x[1])
        t=0
        for d,v in sd:
            if d-(v*t)<=0:
                return t
            t+=1
        return t
        
           
        
        
