class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minVal=prices[0]
        for i in range(len(prices)):
            minVal=min(minVal,prices[i])
            profit=max(profit,prices[i]-minVal)
        return profit