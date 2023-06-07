# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and 
#city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 #UF soltuion
class UF:
    def __init__(self,n):
        self.size = n
        self.par = [i for i in range(self.size)]
        self.rank = [1 for i in range(self.size)]
    def find(self,x):
        while x!= self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x= self.par[x]
        return x
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 != p2:
            if self.rank[p1] >= self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] +=1
            else:
                self.par[p1] = p2
                self.rank[p2] +=1
    def retParent(self):
        return self.par

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        par = [uf.find(i) for i in range(len(isConnected))]
        return len(set(par))
    
#DFS soltion
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    adj[i].append(j)

        def dfs(node,visited):
            if node in visited:
                return 
            visited.add(node)
            for i in adj[node]:
                dfs(i,visited)

        visited = set()
        count = 0
        for i in adj:
            if i not in visited:
                count+=1
                dfs(i,visited)
        return count