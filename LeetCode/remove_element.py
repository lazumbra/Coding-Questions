class Solution:
    def removeElement(self, nums, val):
        iteratorAux = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[iteratorAux] = nums[i]
                iteratorAux+=1
    

        print(nums)
        return(iteratorAux)

if __name__ == "__main__":
    print(Solution().removeElement([3,2,2,3], 3))
