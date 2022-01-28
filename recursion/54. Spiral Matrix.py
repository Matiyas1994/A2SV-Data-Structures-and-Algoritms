class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        stack=[]
        if len(matrix) == 0:
            return []
        for i in range(len(matrix[0])):
            if len(matrix[0])!=0:
                stack.append(matrix[0].pop(0))
        for j in range(1, len(matrix)):
            if len(matrix[j])!=0:
                stack.append(matrix[j].pop())
        for k in range (len(matrix[-1])):
            if len(matrix[-1])!=0:            
                stack.append(matrix[-1].pop())
        for l in range(len(matrix) - 2, 0, -1):
            if len(matrix[l])!=0:
                stack.append(matrix[l].pop(0))
        return stack + self.spiralOrder(matrix[1:-1])
        

        
        ''''
        while matrix:
            for i in range(len(matrix[0])):
                temp=[]
                temp.append(matrix[0].pop())
            stack.extend(reverse(temp))
            for j in range(len(matrix)):
                stack.append(matrix[j].pop())
            for k in range (len(matrix[0])):
                stack.append(matrix[-1].pop())
            for l in range(len(matrix)):
                 stack.append(matrix[l].pop(0))
        '''
      #  return stack
