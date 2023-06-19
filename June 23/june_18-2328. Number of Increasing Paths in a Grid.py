# You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

# Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. 
# Since the answer may be very large, return it modulo 109 + 7.

# Two paths are considered different if they do not have exactly the same sequence of visited cells.


# Input: grid = [[1,1],[3,4]]
# Output: 8
# Explanation: The strictly increasing paths are:
# - Paths with length 1: [1], [1], [3], [4].
# - Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
# - Paths with length 3: [1 -> 3 -> 4].
# The total number of paths is 4 + 3 + 1 = 8.


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = int(1e9 + 7)
        m = len(grid)
        n = len(grid[0])
        
        isValid = lambda x, y: -1 < x < m and -1 < y < n
        
        dp = {}
        def dfs(i, j) -> int:
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = 1
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if isValid(x, y) and grid[x][y] > grid[i][j]:
                    dp[(i,j)] += dfs(x, y)
            return dp[(i,j)] % MOD
            
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD
        return ans