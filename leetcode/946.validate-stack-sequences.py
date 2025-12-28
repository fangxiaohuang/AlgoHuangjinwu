#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        while i < len(pushed) and j < len(popped):
            stack.append(pushed[i])
            i += 1
            if popped[j] == stack[-1]:
                stack.pop()
                j += 1
        while j < len(popped):
            if popped[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                break
        return True if not stack else False
# @lc code=end

