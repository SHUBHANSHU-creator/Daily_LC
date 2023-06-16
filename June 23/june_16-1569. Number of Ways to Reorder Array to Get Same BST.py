# Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) 
# by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that 
# the constructed BST is identical to that formed from the original array nums.

# For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] 
# also yields the same BST but [3,2,1] yields a different BST.


# Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

# Since the answer may be very large, return it modulo 109 + 7.


#soln
#Since its a binary tree you need to keep the order same
# just remember that less comes on left side and greater on the right side
#eg : [3,1,2,5,4,6]
# left side = [1,2], right side = [4,5,6]
#left side can have only one possibility of 1->2, cannot arrange again
#right side can 5,4,6 or 5,6,4 both will give same result but if right side was 4,5,6 then only possibily since all will come on right side
# so call recursive function on both right and left side. If any more combinations can be made then make them by segregating left and 
#right side again

#TC - O(N**2)

import math
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def r(nums):
            mod = 10 ** 9 + 7
            if len(nums) <=2:
                return 1
            left = [num for num in nums if num < nums[0]]
            right = [num for num in nums if num > nums[0]]
            ans = 0
            ans = (math.comb(len(left)+len(right),len(right)) * r(left)*r(right))%mod
            return ans
        return r(nums) -1