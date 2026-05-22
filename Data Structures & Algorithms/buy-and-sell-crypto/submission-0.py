class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxima = 0
        for i in range(len(prices)-1):
            j = i + 1
            while j < len(prices):
                temp = prices[j] - prices[i]
                maxima = max(maxima, temp)
                j += 1
        return maxima