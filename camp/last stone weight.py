import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#         h._heapify_max(stones)
        
#         while len(stones)>=2:
#             e1 = h._heappop_max(stones)
#             e2 = h._heappop_max(stones)
        
#             if e1 != e2:
#                 h.heappush(stones,e1-e2)
                
#             h._heapify_max(stones)
#             print(stones)
                
#         return stones[0] if stones else 0
        
        
        while len(stones)>=2:
            stones .sort()
            e1= stones.pop()
            e2= stones.pop()
            
            if e1 != e2:
                stones.append(e1-e2)
            
        return stones[0] if stones else 0
        
            
