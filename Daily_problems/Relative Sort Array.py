class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        temp=[]
        res=[]
        for i in arr1:
            if i not in arr2:
                temp.append(i)
                arr1.remove(i)
        temp.sort()
        print(temp)
        C=Counter(arr1)
        for i in arr2:
            for j in range(C[i]):
                res.append(i)
        res.extend(temp)
        return  res
