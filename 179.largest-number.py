#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (41.13%)
# Likes:    9127
# Dislikes: 778
# Total Accepted:    726.3K
# Total Submissions: 1.8M
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number and return it.
# 
# Since the result may be very large, so you need to return a string instead of
# an integer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,2]
# Output: "210"
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if x + y < y + x:
                return 1 # 1代表要交换x,y
            return -1

        a = [str(num) for num in nums]
        a.sort(key=functools.cmp_to_key(cmp)) # 按递减排序
        ans = "".join(a)
        if ans[0] == "0": # 处理特殊情况
            return "0"
        return ans
        
# @lc code=end

