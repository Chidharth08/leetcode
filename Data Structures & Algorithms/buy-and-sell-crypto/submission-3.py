class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        maxp = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(profit,maxp)

            else: 
                l = r
            r += 1

        return maxp 
        