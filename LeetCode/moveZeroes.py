class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_it = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_it] = nums[i]
                zero_it+=1

        for i in range(zero_it, len(nums)):
            nums[i] = 0

        
if __name__ == "__main__":
    vetor_ini = [0,1,0,3,12]
    Solution().moveZeroes(vetor_ini)
    print(vetor_ini)
    pass