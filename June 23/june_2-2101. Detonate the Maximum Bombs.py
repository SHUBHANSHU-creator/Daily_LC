# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.


# Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
# Explanation:
# The above figure shows the positions and ranges of the 2 bombs.
# If we detonate the left bomb, the right bomb will not be affected.
# But if we detonate the right bomb, both bombs will be detonated.
# So the maximum bombs that can be detonated is max(1, 2) = 2.

#DFS soltion
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(bombs))}
        for i,(x1,y1,r1) in enumerate(bombs):
            for j,(x2,y2,r2) in enumerate(bombs):
                d = (x2-x1)**2 + (y2-y1)**2
                d = d**(1/2)
                if d <=r1 and i!=j:
                    adj[i].append(j)

        def dfs(node,visited,count):
            visited.add(node)
            count[0] += 1
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei,visited,count)
                    
        mx = 0
        for node in adj:
            visited = set()
            count = [0]
            dfs(node,visited,count)
            mx = max(mx,count[0])
        
        return mx