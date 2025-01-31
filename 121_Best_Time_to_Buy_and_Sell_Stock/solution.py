class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize to infinity (kind of like Dijkstra's)
        max_profit = 0
        
        for price in prices:
            # Update min_price to lowest price encountered so far
            if price < min_price:
                min_price = price
                
            # Calculate profit if sold at the current price
            profit = price - min_price

            # Update max_profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
