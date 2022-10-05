class Solution(object):
    def removeElement(self, nums, val):
        n = 0
        while n != len(nums):
            if nums[n] == val:
                del nums[n]
            else:
                n += 1
        return len(nums)