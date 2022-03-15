class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
       
        visited=[]
        self.tot=0
        
        DIR=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            grid[i][j]=2
            for directions  in DIR:
                nr,nc=i+directions[0],j+directions[1]
                if nr>=0 and nc>=0 and nc<c and nr<r and grid[nr][nc]=='1':
                   
                    dfs(nr,nc)
       
        for i in range(r):
            for j in range(c):
                
                if grid[i][j]=='1' :
                    self.tot+=1
                    
                   
                    dfs(i,j)
     
        return self.tot
