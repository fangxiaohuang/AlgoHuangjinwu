#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (74.25%)
# Likes:    6910
# Dislikes: 1357
# Total Accepted:    1.9M
# Total Submissions: 2.5M
# Testcase Example:  '11'
#
# Given a positive integer n, write a function that returns the number of set
# bits in its binary representation (also known as the Hamming weight).
#
#
# Example 1:
#
#
# Input: n = 11
#
# Output: 3
#
# Explanation:
#
# The input binary string 1011 has a total of three set bits.
#
#
# Example 2:
#
#
# Input: n = 128
#
# Output: 1
#
# Explanation:
#
# The input binary string 10000000 has a total of one set bit.
#
#
# Example 3:
#
#
# Input: n = 2147483645
#
# Output: 30
#
# Explanation:
#
# The input binary string 1111111111111111111111111111101 has a total of thirty
# set bits.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#
# Follow up: If this function is called many times, how would you optimize it?
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        if n & 1 == 1:
            return 1 + self.hammingWeight(n>>1)
        else:
            return self.hammingWeight(n>>1)

# @lc code=end

