class Solution:
     def findCircleNum(self, isconnected: List[List[int]]) -> int:

        r , c = map(len,(isconnected, isconnected[0]))
        graph={}
        for i in range (r):
            graph[i] = []
            for j in range(c):
                if isconnected[i][j] == 1 and i !=j: 
                    graph[i].append(j)
        visited =set()
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)
        
        res = 0
        for i in range(r):
            if i not in visited:
                dfs(i)
                res +=1
        return res
