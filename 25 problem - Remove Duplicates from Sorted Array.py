class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        size = len(nums)

        while size != 1:
            if i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    del nums[i]
                    i -=1
            size -= 1
            i += 1

        return len(nums)