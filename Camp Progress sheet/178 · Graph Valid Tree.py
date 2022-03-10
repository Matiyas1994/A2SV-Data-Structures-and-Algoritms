class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        graph=collections.defaultdict(list)

        if n - len(edges) > 1:
            return False 

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        visited = set()
        count = 0
        cycledectected = False


        def dfs(node,p):
            nonlocal count
            visited.add(node)
            count +=1 
            for v in graph[node]:
                if v != p and v in visited:
                    cycledectected = True
                    return 
                if v not in visited: 
                    dfs(v,node)
        
        dfs(0,-1)
        if count != len(edges) + 1 or cycledectected:
            return False

        return True
