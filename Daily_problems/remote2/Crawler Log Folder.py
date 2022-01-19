class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if i == "../":
                if len(stack)!=0:
                    stack.pop()
                else:
                    continue
            elif i=="./":
                continue
            else:
                stack.append(i[:-1])
        return len(stack)
