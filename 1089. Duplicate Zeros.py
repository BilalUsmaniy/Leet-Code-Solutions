class Solution(object):
    def duplicateZeros(self, arr):

        size = len(arr)
        n = 0
        while n != size:
            if arr[n] == 0 and n != len(arr) - 1:
                arr.insert(n, 0)
                arr.pop()
                n += 1
            n += 1
        return arr