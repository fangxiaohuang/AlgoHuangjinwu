#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        p = 0
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                if i+1 < n and nums[i] == nums[i+1]:
                    nums[i] *= 2
                    nums[i+1] = 0
                    nums[i], nums[p] = nums[p], nums[i]
                    i += 1
                else:
                    nums[i], nums[p] = nums[p], nums[i]
                p += 1
            i += 1
        return nums
        
# @lc code=end

