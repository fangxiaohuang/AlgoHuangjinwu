#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (55.65%)
# Likes:    16980
# Dislikes: 1526
# Total Accepted:    2.2M
# Total Submissions: 4M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        ans = []
        def helper(i1, j1, i2, j2):
            if i2 < i1 or j2 < j1:
                return
            for j in range(j1, j2+1):
                ans.append(matrix[i1][j])
            for i in range(i1+1, i2+1):
                ans.append(matrix[i][j2])
            if i2 > i1:
                for j in range(j2-1, j1-1, -1):
                    ans.append(matrix[i2][j])
            if j2 > j1:
                for i in range(i2-1, i1, -1):
                    ans.append(matrix[i][j1])
            helper(i1+1, j1+1, i2-1, j2-1)

        helper(0, 0, m-1, n-1)

        return ans




# @lc code=end

