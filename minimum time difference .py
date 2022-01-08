from datetime import *
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        tm=[]
        timePoints.sort()
        
        dif2=[]
        for i in range(len(timePoints)):
            d=list(map(int,timePoints[i].split(":")))
            if d[0]*60+d[1]==0:
                tm.append(1440)
            else:
                tm.append(d[0]*60+d[1])
        tm.sort(reverse=True)
        
        for i in range(len(tm)-1):
            for j in range(i+1,len(tm)):
                print(min(abs(tm[i]-tm[j]),abs((1440+tm[j])-tm[i])))
                dif2.append(min(abs(tm[i]-tm[j]),abs((1440+tm[j])-tm[i])))
        
       
        return min(dif2)
        
