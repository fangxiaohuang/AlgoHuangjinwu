#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for num in range(1, n+1):
            ans.append("Push")
            if num == target[i]:
                i += 1
                if i == len(target):
                    break
            else:
                ans.append("Pop")
        return ans
                
        
# @lc code=end

