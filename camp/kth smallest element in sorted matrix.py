import heapq as h
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        rows= len(matrix)
        col = len(matrix[0])
        
        arr=[]
        
        for i in range(rows):
            for j in range(col):
                arr.append(matrix[i][j])
        
        # return arr[k-1]
        h.heapify(arr)
        while k>1:
            h.heappop(arr)
            k-=1
           
        return arr[0]
                
