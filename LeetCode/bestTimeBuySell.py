class Solution:
    def maxProfit(self, prices):
        if len(prices) < 1:
            return 0
        men_value = float('inf')
        max_value = 0

        for i in range(len(prices)):
            if prices[i] < men_value:
                men_value = prices[i]
            else:
                total = prices[i] - men_value
                max_value = max(max_value, total)
        
        return max_value


        

if __name__ == "__main__":
    print(Solution().maxProfit([2, 4, 1]))
    pass