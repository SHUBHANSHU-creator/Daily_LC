# Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

# If there is no way to make arr1 strictly increasing, return -1.

# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].



class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {}
        def dfs(i,prev):
            if i == len(arr1):
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            dp[(i,prev)] = inf
            if prev < arr1[i]:
                dp[(i,prev)] = dfs(i+1,arr1[i])
            nxt_min = bisect.bisect(arr2,prev)
            if nxt_min < len(arr2):
                dp[(i,prev)] = min(dp[(i,prev)],1+dfs(i+1,arr2[nxt_min]))
            return dp[(i,prev)]
        ans = dfs(0,-inf)
        return ans if ans < inf else -1       