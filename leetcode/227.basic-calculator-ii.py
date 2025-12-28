#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (45.65%)
# Likes:    6517
# Dislikes: 947
# Total Accepted:    898.5K
# Total Submissions: 1.9M
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value. 
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        last_op = "+" # ensure the first num is pushed on the stack
        cur_num = 0
        for i in range(n):
            char = s[i]
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            # NOTE Since s[n-1] might be " ", we should not skip processing when encountering " "
            # if char == " ":
            #     continue
            
            # NOTE "if" rather than "elif"
            # Truncate and then process the preceding operation and operands
            if char in ("+", "-", "*", "/") or i == n-1:
                match last_op:
                    case "+":
                        stack.append(cur_num)
                    case "-":
                        stack.append(-cur_num)
                    case "*":
                        stack.append(stack.pop() * cur_num)
                    case "/":
                        stack.append(int(stack.pop() / cur_num)) # truncate towards zero

                cur_num = 0
                if char != " ": # NOTE
                    last_op = char
        print(stack)
        ans = 0
        while stack:
            ans += stack.pop()
        return ans


# @lc code=end

