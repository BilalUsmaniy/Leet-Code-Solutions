class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        count = len(nums)

        if count % 2 != 0:
            median = round(((count / 2) - 0.5))
            return nums[int(median)]
        high_median = int((count / 2))
        low_median = high_median - 1
        median = float((nums[high_median] + nums[low_median]))
        return median / 2