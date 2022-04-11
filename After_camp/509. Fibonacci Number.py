class Solution:
    def fib(self, n: int) -> int:
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)
        
#         if n==0:
#              return 0
            
#         pre1,curr =1,1
#         for i in range(2,n):
#             temp = curr
#             curr +=pre1
#             pre1 = temp
        
#         return curr 
        memo={1:1,0:0}
        def fibo(n):
            if n in memo:
                return memo[n]
            memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]
            
        return fibo(n)
