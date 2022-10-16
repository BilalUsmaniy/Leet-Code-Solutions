class Solution(object):
    def countDistinctIntegers(self, nums):
        res = set(nums)
        for i in nums:
            x = int(str(i)[::-1])
            res.add(x)
        return len(res)
