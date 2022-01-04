class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda a:a[0])
        new=[]
        s=intervals[0][0]
        e=intervals[0][1]
        for j in range( len(intervals)):
            if e >= intervals[j][0]:
                e = max(e,intervals[j][1])
            else:
                new.append([s,e])
                s=intervals[j][0]
                e=intervals[j][1]
        
        new.append([s, e])
        return new
