#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (48.72%)
# Likes:    5594
# Dislikes: 477
# Total Accepted:    239.7K
# Total Submissions: 490.8K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# You are given an array of binary strings strs and two integers m and n.
# 
# Return the size of the largest subset of strs such that there are at most m
# 0's and n 1's in the subset.
# 
# A set x is a subset of a set y if all elements of x are also elements of
# y.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10",
# "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the
# maximum of 3.
# 
# 
# Example 2:
# 
# 
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] # dp[i][j][k]: 前i个str，在j个0和k个1的容量下的最大值

        def count(s):
            cnt0, cnt1 = 0, 0
            for c in s:
                if c == "0": cnt0 += 1
                else: cnt1 += 1
            return cnt0, cnt1

        for i in range(1, l+1):
            cnt0, cnt1 = count(strs[i-1])
            for j in range(m, cnt0-1, -1):
                for k in range(n, cnt1-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-cnt0][k-cnt1] + 1) # NOTE +1是重点
        return dp[m][n]
                    
        
# @lc code=end

