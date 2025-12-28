#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0 # point to next non-zero element
        for i, num in enumerate(nums):
            if num != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        
        
# @lc code=end

