class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['+','-','*','/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                x=stack.pop()
                y=stack.pop()
                if i =='+':
                    stack.append(x+y)
                elif i=='-':
                    stack.append(y-x)
                elif i=='*':
                    stack.append(x*y)
                elif i=='/':
                    stack.append(int(y/x))
        return stack.pop()
                    
                
