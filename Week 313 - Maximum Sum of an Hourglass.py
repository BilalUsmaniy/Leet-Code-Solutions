class Solution(object):
    def maxSum(self, grid):
        max_val = 0

        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                variable1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] + \
                            grid[i + 2][j + 1] + grid[i + 2][j + 2]
                if variable1 > max_val:
                    max_val = variable1

        return max_val