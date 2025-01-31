class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        # Iterate over prices list and calculate profit when price increases
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
