class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k=k%len(nums)
        
        num=nums.copy()

        p1=len(nums)-k
        i=0

        while p1<len(nums):
            nums[i]=num[p1]
            i+=1
            p1+=1
        p1=0

        while i < len(nums):
            nums[i] = num[p1]
            i+=1
            p1+=1
