class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack=[]
        dicti={}
        output=[]
        for i in reversed(range(len(nums2))):
           
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if len(stack)==0:
                dicti[nums2[i]]=-1
            else:
                dicti[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        
        
        
        return [dicti[i] for i in nums1 if i in dicti]
