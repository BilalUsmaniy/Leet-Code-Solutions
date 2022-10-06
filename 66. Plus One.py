class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        llist = list(map(str, digits))
        num = ''
        for i in llist:
            num += i
        num = int(num) + 1
        num = list(str(num))
        return num