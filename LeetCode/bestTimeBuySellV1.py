class Solution:
    def maxProfit(self, prices):
        if len(prices) < 1:
            return 0
        
        totalProfit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                thisProfit = prices[i+1] - prices[i]
                totalProfit += thisProfit
        return totalProfit

if __name__ == "__main__":
    print(Solution().maxProfit([7,6,4,3,1]))
