class Solution:
    def moveZeroes(self, nums):
        iterador = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                aux = nums[iterador]
                nums[iterador] = nums[i]
                iterador+=0
            print(nums[i])
        """
        Do not return anything, modify nums in-place instead.
        """

if __name__ == "__main__":
    Solution().moveZeroes([0,1,0,3,12])
    pass