class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations += [0]
        citations.sort()
        l = len(citations)
        res = 0
        for i in range(len(citations)-1,-1,-1):
            h = l-i
            if citations[i] >= h and citations[i-1] <= h:
                res = h
                
        return res
