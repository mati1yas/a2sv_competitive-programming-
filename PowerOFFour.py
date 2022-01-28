class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def mypowFour(x):
           
            if x==1:
                return True
            if x>=0 and x<1:
                return False
            
            
            return mypowFour(x/4)
        return mypowFour(n)
