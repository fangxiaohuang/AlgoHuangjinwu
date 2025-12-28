#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (51.98%)
# Likes:    36217
# Dislikes: 1535
# Total Accepted:    5.2M
# Total Submissions: 10M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        minsum = [0] * (n+1)
        for i in range(1, n+1):
            minsum[i] = min(minsum[i-1], presum[i])

        ans = float("-inf") # NOTE
        for i in range(1, n+1):
            ans = max(ans, presum[i] - minsum[i])
        return ans
# @lc code=end

