class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image[sr][sc] == newColor:
            return image
        
        def filler(r,c):
            if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or start != image[r][c]:
                return 
            image[r][c]=newColor
            filler(r+1,c)
            filler(r-1,c)
            filler(r,c+1)
            filler(r,c-1)
            
        start=image[sr][sc]
        
        filler(sr,sc)
        return image
