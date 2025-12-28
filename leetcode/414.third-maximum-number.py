#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from sortedcontainers import SortedSet
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        tree_set = SortedSet() # ascending order by default
        for num in nums:
            tree_set.add(num)
        if len(tree_set) >= 3:
            return tree_set[-3]
        else:
            return tree_set[-1]
        
# @lc code=end

