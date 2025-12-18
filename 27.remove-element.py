#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # number of val to be removed, starts from 0
        for i, num in enumerate(nums):
            if num == val:
                k += 1
            else:
                nums[i-k] = num
        return len(nums) - k
# @lc code=end

