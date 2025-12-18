#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start

class BIT:
    def __init__(self, n) -> None:
        self.n = n
        self.tree = [(1, 1)] * (n+1) # (max_len, count)

    def lowbit(self, i):
        return i & -i

    def update(self, i, max_len, count): # 将当前i结尾的数组里的最长递增子序列的长度和个数更新为max_len和count: 不是sum()，是max()
        while i <= self.n:
            i += self.lowbit(i)

    def query(self, i): # 查询以当前i结尾的数组里的最长递增子序列的长度和个数
        max_len, count = 1, 1
        while i >= 1:
            i -= self.lowbit(i)


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
# @lc code=end

