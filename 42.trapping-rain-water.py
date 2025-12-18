#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (64.83%)
# Likes:    34459
# Dislikes: 615
# Total Accepted:    2.9M
# Total Submissions: 4.5M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # 递减栈: 栈底到栈顶递减
        ans = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h: # 新元素入栈时，弹出所有小于等于它的元素
                j = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                    ans += (min(h, height[stack[-1]]) - height[j]) * width
            stack.append(i)
        return ans

# @lc code=end

