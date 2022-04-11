class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx=[0 for _ in range(len(prices))]
        maxx[len(prices)-1]=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            maxx[i] = max(maxx[i+1],prices[i])
        
       
        profit = float(-inf)
        for i in range(len(prices)):
            p = maxx[i] - prices[i]
            profit = max(profit,p)
        return profit
