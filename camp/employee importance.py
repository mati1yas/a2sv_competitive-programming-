
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {}
        
        for employee in  employees:
            dic[employee.id ]= employee
        self.imp_total=0
        
        def dfs (employee):            
            self.imp_total+=employee.importance
            
            for i in employee.subordinates:
                dfs(dic[i])
       
        dfs(dic[id])
        return self.imp_total
            
            
