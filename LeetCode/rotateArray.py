class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums = nums[::-1]
        k = k % len(nums)
        print('k', k)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

array1 = [1,2]

Solution().rotate(array1, 3)
print(array1)