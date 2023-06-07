# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Input: grid = [[0,1],[1,0]]
# Output: 2

#BFS solution
from collections import defaultdict,deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        if grid[0][0] == 1:
            return -1
        q.append((0,0,1))
        direct = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        visited = set()
        while q:
            for i in range(len(q)):
                r,c,moves = q.popleft()
                if r== n-1 and c == n-1:
                    return moves
                for dr,dc in direct:
                    newR,newC = r+dr,c+dc
                    if (min(newR,newC) >= 0 and max(newR,newC) < n ) and grid[newR][newC] == 0 and (newR,newC) not in visited:
                        q.append((newR,newC,moves+1))
                        visited.add((newR,newC))
        return -1