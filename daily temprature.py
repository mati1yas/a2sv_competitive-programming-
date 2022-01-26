class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for index,item in enumerate(temperatures):
            while stack and item>stack[-1][0]:
                stackt,stackin=stack.pop()
                print(stackt,stackin)
                res[stackin]=(index-stackin)
            stack.append([item,index])
        return res
            
