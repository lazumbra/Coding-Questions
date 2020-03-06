class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[1], nums[0])
        
        aux_robber = [0] * len(nums)
        aux_robber[0] = nums[0]
        aux_robber[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            aux_robber[i] = max(nums[i]+aux_robber[i-2], aux_robber[i-1])
        return aux_robber[-1]


if __name__ == "__main__":
    print(Solution().rob([1,3, 1]))
    pass
        