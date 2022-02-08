class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1=0
        p2= 0
        

#         zero_counter = 0
#         non_zeros = []
#         p1 = 0
#         while p1 < len(nums):
#             if nums[p1] != 0:
#                 non_zeros.append(nums[p1])
#             else:
#                 zero_counter += 1
#             p1 += 1
#         nums = non_zeros + [0]*zero_counter
        
#         return nums
        while p2 < len(nums):
            if nums[p2] != 0 :
                nums[p1] = nums[p2]
                p1+=1
                p2+=1
            else:
                p2+=1
                
        for p1 in range(p1,p2):
            nums[p1]=0

