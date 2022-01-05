class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        s=list(s)
        s.sort()
        for i in range(len(s)):            
            nums[i]=s[i]
        
        return len(s)
        
