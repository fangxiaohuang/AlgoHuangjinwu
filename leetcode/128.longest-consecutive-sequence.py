#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ans = 0
        # 遍历穷举是写代码的精髓，要充分利用计算机的计算优势
        for num in nums:
            if num-1 in hashset:
                continue
            # 从当前数字开始遍历穷举，直到找不到连续的数字为止
            p = num
            count = 0
            while p in hashset:
                count += 1
                p += 1
            ans = max(ans, count)
        return count
# @lc code=end

