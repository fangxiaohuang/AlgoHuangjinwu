#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (47.09%)
# Likes:    18474
# Dislikes: 343
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
#
#
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
#
#
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # 单调递增栈: 新增元素时, ≥它的元素都要弹出
        ans = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                j = stack.pop()
                if stack:
                    width = i - stack[-1] - 1 # i为右边界, stack[-1]为左边界, 方框区域不包括i和stack[-1]
                    ans = max(ans, width*h)
            stack.append(i)
        return ans


# @lc code=end

