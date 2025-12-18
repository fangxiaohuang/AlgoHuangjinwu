#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.58%)
# Likes:    9466
# Dislikes: 2136
# Total Accepted:    1M
# Total Submissions: 2.4M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# You are given an m x n matrix board containing letters 'X' and 'O', capture
# regions that are surrounded:
#
#
# Connect: A cell is connected to adjacent cells horizontally or
# vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the
# region with 'X' cells and none of the region cells are on the edge of the
# board.
#
#
# To capture a surrounded region, replace all 'O's with 'X's in-place within
# the original board. You do not need to return anything.
#
#
# Example 1:
#
#
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Explanation:
#
# In the above diagram, the bottom region is not captured because it is on the
# edge of the board and cannot be surrounded.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
#
# Output: [["X"]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
#
#
#

# @lc code=start
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(i, j):
            dq = deque()
            dq.append((i, j))
            while dq:
                i, j = dq.pop()
                board[i][j] = "#"
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "O":
                        dq.append((ni, nj))

        for i in range(m):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][n-1] == "O":
                bfs(i, n-1)
        for j in range(1, n-1):
            if board[0][j] == "O":
                bfs(0, j)
            if board[m-1][j] == "O":
                bfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


# @lc code=end

