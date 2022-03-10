class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dic = {}
        
        for i in range(len(isConnected)):
            dic[i]=[]
            for j in range(len(isConnected[0])):
                if isConnected[i][j] ==1 and i!=j:
                     dic[i].append(j)
        visited=set()
        self.prov=0
        def dfs(connection):
            visited.add(connection)
            for i in dic[connection]:
                if i not in visited:
                    dfs(i)
            
        for i in dic.keys():
            if i not in visited:
                dfs(i)
                self.prov+=1
        
        return self.prov
