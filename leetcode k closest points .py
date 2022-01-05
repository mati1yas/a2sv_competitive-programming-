import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d=[]
        c=0
        for i in range(len(points)):
            d.append(math.sqrt(pow(points[i][0],2)+pow(points[i][1],2)))    
        mydict=dict(zip(d,points))
        
        points.clear()
        for i in sorted(mydict.keys()):
            points.append(mydict[i])
            c+=1
            if c==k:
                break
        
        
        return points
