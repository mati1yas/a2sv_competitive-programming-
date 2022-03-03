import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
#       USING MIN HEAP 
#         h.heapify(nums)
        
#         while len(nums)>k:
#             h.heappop(nums)
            
            
#         return nums[0]


# using MAX HEAP

#         h._heapify_max(nums)
        
#         while k>1:
#             var=h.heappop(nums)
#             h._heapify_max(nums)
#             print(nums)
#             print(var)
#             k-=1
            
            
#         return nums[0]



        h._heapify_max(nums)
        
        while k>0:
            var=h.heappop(nums)
            h._heapify_max(nums)
            
            k-=1
            
            
        return var
