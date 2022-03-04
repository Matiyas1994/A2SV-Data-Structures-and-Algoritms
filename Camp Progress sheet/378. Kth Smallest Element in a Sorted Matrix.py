    
        class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a= []
        n = len(matrix) 
        for i in range(n):
            for j in range(n):
                a.append(matrix[i][j])
        
        heapq.heapify(a)
        return heapq.nsmallest(k,a)[-1]
