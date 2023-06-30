# There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and 
# col representing the number of rows and columns in the matrix, respectively.

# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. 
# You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on 
# the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. 
# You can start from any cell in the top row and end at any cell in the bottom row. You can only travel 
# in the four cardinal directions (left, right, up, and down).

# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.



# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.




#solution
#Using binary search to check if on the middle day we can traverse
#TC - O(BFS/DFS)*O(log(cells.size)) => O(row*col) * O(log(row*col)) => O(10**4) * O(log(10**4))

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        direct = [[-1,0],[1,0],[0,-1],[0,1]]
        def possible(dayat):
            visited =set()
            grid = [[0 for j in range(col)] for i in range(row)]
            for i in range(dayat):
                x,y = cells[i][0],cells[i][1]
                grid[x-1][y-1] = 1
            q = deque()
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0,c))
                    visited.add((0,c))
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    if r == row - 1:
                        return True
                    for dr,dc in direct:
                        newR,newC = r+dr, c+dc
                        if 0<=newR<row and 0<=newC<col and (newR,newC) not in visited and grid[newR][newC] == 0:
                            visited.add((newR,newC))
                            q.append((newR,newC))
            return False

        l = 1
        r = len(cells)
        ans = 0
        while l<=r:
            mid = (l+r)>>1
            if possible(mid):
                ans = mid
                l = mid+1
            else:
                r = mid -1
        return ans