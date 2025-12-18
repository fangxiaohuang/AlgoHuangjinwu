#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (80.66%)
# Likes:    18178
# Dislikes: 307
# Total Accepted:    2.5M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, x = [], []
        n = len(nums)

        def dfs(x, i):
            if i == n:
                ans.append(x[:]) # NOTE deep copy
                return
            # Choose
            x.append(nums[i])
            dfs(x, i+1)
            # Do not choose
            x.pop()
            dfs(x, i+1)

        dfs(x, 0)
        return ans

# @lc code=end

