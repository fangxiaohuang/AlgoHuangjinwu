#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 栈底存放最近一段的右括号的位置
        stack = [-1]
        ans = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                # 尝试匹配"("
                stack.pop()

                if stack:
                    # 匹配成功，栈底还有右括号
                    ans = max(ans, i - stack[-1])
                else:
                    # 匹配失败，将右括号入栈
                    stack.append(i)
        return ans

        
# @lc code=end

