class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        l=[int(x) for x in nums]     
        l.sort(reverse=True)
        p=str(l[k-1])
        
        return p

        
