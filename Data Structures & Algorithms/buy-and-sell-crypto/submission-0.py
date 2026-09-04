class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minval=prices[0]
        for sell in prices:
            profit=max(profit,sell-minval)
            minval=min(minval,sell)
        return profit
