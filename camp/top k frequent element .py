import heapq as h
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        arr =[ (count[x],x) for x in count .keys()]
    
        
        h.heapify(arr)
        while len(arr)>k:
            h.heappop(arr)
        
        
            
        return [j for i,j in arr ]
            
                
