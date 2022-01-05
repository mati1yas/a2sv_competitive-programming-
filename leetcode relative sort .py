class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s=[]
        for i in arr2:
            for j in range(len(arr1)):
                if arr1[j]==i:
                    s.append(arr1[j])
        for i in sorted(arr1)  :
            if i not in arr2:
                s.append(i)
        return s
