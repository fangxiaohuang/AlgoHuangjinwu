#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (37.30%)
# Likes:    6264
# Dislikes: 159
# Total Accepted:    259K
# Total Submissions: 693.6K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
#
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
#
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
#
# Note: You cannot rotate an envelope.
#
#
# Example 1:
#
#
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
#
#
# Example 2:
#
#
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5
#
#
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1])) # width asc and height desc to calculate LIS of height
        heights = [e[1] for e in envelopes]
        return self.length_of_LIS(heights)

    def length_of_LIS(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n-1]



# @lc code=end

