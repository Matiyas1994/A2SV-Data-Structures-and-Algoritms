class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        res=[0 for i in range(len(temperatures))]
        stack=[]
        for i in range(len(temperatures)):
            if not stack:
                stack.append(temperatures[i])
            else:
                while stack and stack[-1] < temperatures[i]:
                    c=stack.pop()
                    res[temperatures.index(c)]=i-temperatures.index(c)   
                stack.append(temperatures[i])
        return res
        '''
        res = [0] * len(temperatures)
        stack = []
        p = len(temperatures)-1
        
        while p >= 0:
            while stack and temperatures[p] >= temperatures[stack[-1]]: 
                stack.pop()
            if stack:
                res[p] = stack[-1] - p
            
            stack.append(p)
            p -=1
        return res
            
