class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        queue = deque()
        visited = set()

        m , n =map(len,(board,board[0]))
        neighbour = [(1,0),(-1,0),(0,1),(0,-1)]
        
    
        for j in range(n):
            if  board[0][j]=="O":
                queue.append((0,j))
                visited.add((0,j))
            if board[m-1][j]=="O":
                queue.append((m-1,j))
                visited.add((m-1,j))
        for i in range(1,m-1):
            if board[i][0] =="O":
                queue.append((i,0))
                visited.add((i,0))
            if board[i][-1]=="O":
                queue.append((i,n-1))
                visited.add((i,n-1))
        
     
        while queue:
                i , j = queue.popleft()
                for c,r in neighbour:
                    newRow, newCol = c + i ,  r + j 
                    if 0<=newRow<m and 0<= newCol <n and (newRow,newCol) not in visited and board[newRow][newCol]=="O" :
                        visited.add((newRow,newCol))
                        queue.append((newRow,newCol))
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    board[i][j] = "X"
           
