# https://leetcode.com/problems/merge-sorted-array/submissions/ 

s=0
        
for i in range(len(nums1)):
    for j in range(s,len(nums2)):
        if nums1[i]==0:
            nums1[i]=nums2[j]
            s+=1
            break   
nums1=nums1.sort()
