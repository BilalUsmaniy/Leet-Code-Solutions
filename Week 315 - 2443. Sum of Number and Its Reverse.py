class Solution(object):
    def sumOfNumberAndReverse(self, num):
        for i in range(num):
            if i + int(str(i)[::-1]) == num:
                return True
        if num == 0:
            return True
        else:
            return False
