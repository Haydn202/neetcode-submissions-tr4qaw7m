class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        profit = 0

        buy = prices[0]

        for i in range(len(prices)):
            current = prices[i] - buy
            profit = max(current, profit)

            if prices[i] < buy:
                buy = prices[i]
            
        return profit

