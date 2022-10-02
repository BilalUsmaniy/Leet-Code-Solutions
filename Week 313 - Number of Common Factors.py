class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        biggest = max(a, b)

        nums = []
        for i in range(1, biggest + 1):
            if a % i == 0 and b % i == 0:
                nums.append(i)
        return len(nums)
