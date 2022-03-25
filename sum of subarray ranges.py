class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        r=0
        for i in range (len(nums)):            
            for j in range(i,len(nums)):
                if i==j:    
                    mini=nums[i]
                    maxi=nums[i]
                    
                else:
                    mini=min(mini,nums[j])
                    maxi=max(maxi,nums[j])                   
                    r+=maxi-mini
                    
                    
                    
        return r
