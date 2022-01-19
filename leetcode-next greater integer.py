class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.reverse()
        nums2.reverse()
        greater=0
        s1=0
        e=0
        s2=0
        new =[]
        n1=nums1.copy()
        n2=[]
        for i in range (len(nums1)):
            n2=nums2.copy()
            greater=0
            if len(n1)!=0: 
                s1=n1.pop()
            for j in range(len(nums2)):
                if len(n2)!=0: 
                    s2=n2.pop()
                if s1==s2 :
                    while( len(n2)!=0):
                        e=n2.pop()
                        if e>s1:
                            greater=e
                            break
                if (greater==0 and len(n2)==0):
                    greater=-1
                
                    
                
            new.append(greater)
        return new
                
        
