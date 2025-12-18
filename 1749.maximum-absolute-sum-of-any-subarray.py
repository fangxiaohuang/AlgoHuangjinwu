#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        presum, maxpre, minpre = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            presum += num
            maxpre = max(maxpre, presum)
            minpre = min(minpre, presum)
        if minpre >= 0:
            return maxpre
        elif maxpre <= 0:
            return abs(minpre)
        else:
            return maxpre - minpre
            
        
# @lc code=end

