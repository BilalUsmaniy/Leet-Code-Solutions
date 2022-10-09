class Solution(object):
    def countEven(self, num):
        res = 0
        for i in range(1, num + 1):
            num_sum = sum(list(map(int, str(i))))
            if num_sum % 2 == 0:
                res += 1
        return res