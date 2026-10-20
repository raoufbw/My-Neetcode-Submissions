class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(1,len(prices)):
            for k in range(i):
                p = prices[i] - prices[k]
                if p > max_p:
                    max_p = p
        return max_p
