#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for c in s:
            if ans and c.lower() == ans[-1].lower() and c != ans[-1]:
                ans.pop()
            else:
                ans.append(c)
        return "".join(ans)
        
# @lc code=end

