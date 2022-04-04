class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # build adjecency list 
        # use dfs or bfs from the source node
        # if path found return true else false
        
        graph={}
        
        for e in  edges:
            if e[0] not in graph:
                graph[e[0]] = []
            graph [e[0]].append(e[1])
            if e[1] not in graph:
                graph[e[1]] = []        
            graph[e[1]].append(e[0])
        
        
        visited = set()
        found = False
        def dfs(s):
            nonlocal destination,visited,found
            visited.add(s)
            if s == destination:
                found = True
                return
            for node in graph[s]:
                if node not in visited:
                    dfs(node)
        
        dfs(source)
        return found
