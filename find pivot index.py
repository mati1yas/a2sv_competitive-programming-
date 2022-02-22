// it fails the last test case out 743 test cases
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if sum(nums[0:i])== sum(nums[i+1:len(nums)]):
                return i
            elif i==len(nums)-1:
                return -1
            
        return 0
