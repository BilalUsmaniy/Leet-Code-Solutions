class Solution(object):
    def majorityElement(self, nums):
        output = {}
        for i in nums:
            if output.get(i):
                output[i] += 1
            else:
                output[i] = 1
        majority_element = max(output, key=output.get)
        return majority_element
