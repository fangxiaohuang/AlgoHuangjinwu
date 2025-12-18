#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (61.67%)
# Likes:    6898
# Dislikes: 169
# Total Accepted:    623.8K
# Total Submissions: 1M
# Testcase Example:  '[[2,1,3],[6,5,4],[7,8,9]]'
#
# Given an n x n array of integers matrix, return the minimum sum of any
# falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element
# in the next row that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col
# - 1), (row + 1, col), or (row + 1, col + 1).
#
#
# Example 1:
#
#
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
#
#
# Example 2:
#
#
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
#
#
#
# Constraints:
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
#
#
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        INF = float("inf")
        m, n = len(matrix), len(matrix[0])
        dp1 = matrix[0][:]
        directions = [-1, 0, 1]
        for i in range(1, m):
            dp2 = [INF] * n
            for j in range(n):
                for dj in directions:
                    nj = j + dj
                    if 0 <= nj < n:
                        dp2[j] = min(dp2[j], dp1[nj])
                dp2[j] += matrix[i][j]
            dp1 = dp2[:]
        return min(dp1)


# @lc code=end

