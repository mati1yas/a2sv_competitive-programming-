
class KthLargest:

    def __init__(self,k: int, nums: List[int]):
        self.nums=[x for x in nums]
        self.arr=[]
        self.k=k
        
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()        
        return self.nums[-self.k]
      
import  heapq as h
class KthLargest:

    def __init__(self,k: int, nums: List[int]):
        self.nums=[x for x in nums]
        self.arr=[]
        self.k=k
        h._heapify_max(self.nums)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        
        h.heappush(self.nums,val)
        
        while len(self.nums)>self.k:
            h.heappop(self.nums)
            print(self.nums)
            
        
        return self.nums[0]
            
