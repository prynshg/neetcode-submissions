class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minval=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minval:
                minval=prices[i]
            profit=max(profit,prices[i]-minval)

        return profit
