class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict={}
        mydict[0]=1
        prefix_sum = 0
        counter = 0
        
        for i in nums:
            prefix_sum += i 
            if prefix_sum - k in mydict:
                counter += mydict[prefix_sum-k]
                        
            if prefix_sum in mydict:
                mydict[prefix_sum]+=1
            else:
                mydict[prefix_sum]=1
        return counter
