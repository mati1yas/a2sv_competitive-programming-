class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=[]
        [n.append(pow(int(x),2)) for x in nums]
        n.sort()
        return n
        
