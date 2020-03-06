class Solution:
    def rob(self, nums):
        total1 = 0
        total2 = 0

        for i in range(0,len(nums), 2):
            total1+=nums[i]
            if i+1 < len(nums):
                print(len(nums))
                total2 += nums[i+1]
        
        if total1 > total2:
            return total1
        else:
            return total2

if __name__ == "__main__":
    print(Solution().rob([1,3,1]))
    pass
        