class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def profitcalc(i,choice):
            # nonlocal profit
            if i >= len(prices):
                return 0
            if (choice,i) in memo:
                return memo[(choice,i)]
            m = 0
            if choice=="cooldown":
                m=max(profitcalc(i+1,choice), profitcalc(i+1,"buy")-prices[i])
            
            elif choice=="sell":
                m = profitcalc(i+1,"cooldown")
            
            elif choice =="buy":
                m = max(profitcalc(i+1,"sell")+ prices[i], profitcalc(i+1,"buy"))
            memo[(choice,i)]=m
            return m
        
         
        return profitcalc(0,"cooldown")
