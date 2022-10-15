class Solution(object):
    def findOcurrences(self, text, first, second):

        text = text.split()
        res = []
        for i in range(len(text)):
            if i + 2 < len(text) and text[i] == first and text[i + 1] == second:
                res.append(text[i + 2])

        return res