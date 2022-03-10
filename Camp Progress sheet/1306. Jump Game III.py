class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = deque()
        
        visited = set()
        arrlen = len(arr)
        queue.append(start)
        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            new1 = i + arr[i]
            new2 = i - arr[i]
            
            if 0<= new1 < arrlen and new1 not in visited:
                queue.append(new1)
                visited.add(new1)
            if 0<=new2 < arrlen and new2 not in visited:
                queue.append(new2)
                visited.add(new2)
            
        return 
