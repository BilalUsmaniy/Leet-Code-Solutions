class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_dict = {}
        for i in nums:
            if my_dict.get(i):
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        min_value = min(my_dict.values())

        return list(my_dict.keys())[list(my_dict.values()).index(min_value)]
