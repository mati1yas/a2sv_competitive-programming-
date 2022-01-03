class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        counter=0
    
        Sorted=sorted(heights)
        
        for i in range(len(heights)):
            if Sorted[i]!=heights[i]:
                counter+=1
        return counter
