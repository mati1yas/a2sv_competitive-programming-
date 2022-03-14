class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        r = len(grid)
        c = len(grid[0])
     
        self.tot=0
        maxi=0
        DIR = [[0,1],[1,0],[0,-1],[-1,0] ]
        def dfs(x,y):
            self.tot+=1
            grid[x][y] = 0 
            
           
            for directions in DIR:
                x2 = x+directions[0] 
                y2 = y+directions[1]
                if x2 >= 0 and y2 >= 0 and x2 < r and y2 < c and grid[x2][y2] == 1:
                    dfs(x2, y2) 
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 1: 
                    self.tot=0
                    dfs(x,y)
                    
                    maxi = max(self.tot,maxi)
                    
        
        return maxi
