class Solution(object):
    def smallestEvenMultiple(self, n):
        a = n
        while True:
            if a % 2 == 0 and a % n == 0:
                break
            a += 1
        return a
