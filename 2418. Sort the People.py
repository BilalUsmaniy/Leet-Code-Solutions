class Solution(object):
    def sortPeople(self, names, heights):

        dict1 = {}
        for i, j in zip(heights, names):
            dict1[i] = j
        k = sorted(dict1)[::-1]
        res = []
        for i in k:
            res.append(dict1[i])
        return res