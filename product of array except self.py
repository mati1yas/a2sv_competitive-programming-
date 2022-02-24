class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = 0
        index = 0
        product = 1
        ans = [0] * len(nums)
        
        if 0 not in nums:
            for i in nums:
                product *= i
            for i in range (len(nums)):
                ans[i] = product//nums[i]
            return ans
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    product *= nums[i]
                    
                else:
                    index =i
                    c += 1
                    
                if c>1:
                    return [0]*len(nums)
            ans[index]= product 
            return ans
