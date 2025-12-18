#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap[0] = -1 # 余数为0第一次出现的下标为-1
        presum = 0
        for i, num in enumerate(nums):
            presum = (presum + num) % k
            if presum in hmap:
                if j - hmap[presum] + 1 > 2:
                    return True
            hmap[presum] = i
        return False


        
# @lc code=end

