class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                k=""
                c=0
                while(stack[-1]!='('):
                    k +=stack.pop()
                    c +=1
                stack.pop()
                for j in range(c):
                    stack.append(k[j])
        res=''.join(map(str, stack))
        return res
        
