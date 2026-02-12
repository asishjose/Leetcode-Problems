class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b = 0
        maxProfit = 0
        for s in range(n):
            if prices[s]>prices[b]:
                profit = prices[s] - prices[b]
                maxProfit = max(maxProfit, profit)
            else:
                b = s
        return maxProfit
            