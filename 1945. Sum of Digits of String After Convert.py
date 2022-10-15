class Solution(object):
    def getLucky(self, s, k):

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z']

        nums = ''
        for i in s:
            nums += str(letters.index(i) + 1)
        output = sum([int(i) for i in nums])

        if k > 1:
            for i in range(1, k):
                output = sum(map(int, str(output)))
            return output
        else:
            return output