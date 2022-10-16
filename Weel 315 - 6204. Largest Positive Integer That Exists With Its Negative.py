class Solution(object):
    def findMaxK(self, nums):
        while len(nums) != 0:
            largest = max(nums)
            if -abs(largest) in nums and abs(largest) in nums:
                return largest
            nums.remove(largest)
        return -1