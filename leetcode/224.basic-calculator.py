#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (45.37%)
# Likes:    6822
# Dislikes: 549
# Total Accepted:    651.6K
# Total Submissions: 1.4M
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
# Example 1:
#
#
# Input: s = "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: s = " 2-1 + 2 "
# Output: 3
#
#
# Example 3:
#
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is
# invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is
# valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.
#
#
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        ans, i = 0, 0
        sign = 1
        stack = [1]
        while i < n:
            if s[i] == " ":
                i += 1
                continue

            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            ans += sign * num

            if i >= n: break
            match s[i]:
                case "+":
                    sign = stack[-1] * +1
                case "-":
                    sign = stack[-1] * -1
                case "(":
                    stack.append(sign)
                case ")":
                    stack.pop()
            i += 1

        return ans


# @lc code=end

