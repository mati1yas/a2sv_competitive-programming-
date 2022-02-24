class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0 
        i = 0
        long = 0
        recency = {}
        while i < len(fruits):
            recency[fruits[i]] = i
            if len(recency)>=3:
                least_recent = min(recency.values())
                start = least_recent + 1
                del recency[fruits[least_recent]]
            long=max (long, i-start+1)
            i+=1
        return long
