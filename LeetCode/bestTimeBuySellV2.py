#https://www.urionlinejudge.com.br/judge/en/problems/view/1932
class Solution:
    def maxProfit(self, prices, k):
        if len(prices) < 1:
            return 0
        men_value = float('inf')
        max_value = 0
        indMenor = 0

        for i in range(0, len(prices)-1):
            #print('preços: ',prices[i+1])
            if prices[i+1] > prices[indMenor]:
                print(i+1)
                indMenor = i+1
            else:
                indMenor = i+1

        for i in range(len(prices)):
            if prices[i] < men_value:
                men_value = prices[i]
            else:
                total = prices[i] - men_value
                max_value = max(max_value, total)
        
        return max_value


        

if __name__ == "__main__":
    print(Solution().maxProfit([10, 80, 20, 40, 30, 50, 40, 60, 50, 70, 60, 10, 200], 30))
    pass
    #13 30
    #