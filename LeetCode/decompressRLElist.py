from typing import List

def decompressRLElist(self, nums: List[int]) -> List[int]:
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    list_out = list()
    for i in range(0, len(nums)-1, 2):
        for j in range(nums[i]):
            list_out.append(nums[i+1])
    return list_out

if __name__ == '__main__':
    print(decompressRLElist([1, 2, 3,4]))
    print('oi')


