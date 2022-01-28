class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def mypow(x):
           
            if x==1:
                return True
            if x>=0 and x<1:
                return False
            
            
            return mypow(x/3)
        return mypow(n)
