#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split("/")
        stack = []
        for item in items:
            s = item.strip()
            if s in ["", "."]:
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)
        
# @lc code=end

