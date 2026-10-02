class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minVal=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minVal:
                minVal=prices[i]
            profit=max(profit,prices[i]-minVal)
        return profit