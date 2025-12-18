#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (58.53%)
# Likes:    5593
# Dislikes: 217
# Total Accepted:    244K
# Total Submissions: 416.6K
# Testcase Example:  '[[0,1],[1,0]]'
#
# You are given an n x n binary matrix grid where 1 represents land and 0
# represents water.
#
# An island is a 4-directionally connected group of 1's not connected to any
# other 1's. There are exactly two islands in grid.
#
# You may change 0's to 1's to connect the two islands to form one island.
#
# Return the smallest number of 0's you must flip to connect the two
# islands.
#
#
# Example 1:
#
#
# Input: grid = [[0,1],[1,0]]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
#
#
# Example 3:
#
#
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
#
#
#
# Constraints:
#
#
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
#
#
#

# @lc code=start
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        land = set()
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i, j):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and visited[ni][nj] == False:
                    visited[ni][nj] = True
                    land.add((ni, nj))
                    dfs(ni, nj)

        find = False
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == 1:
                    land.add((i, j))
                    visited[i][j] = True
                    dfs(i, j)
                    find = True
                    break
            if find == True:
                break

        def bfs():
            dq = deque()
            for i, j in land:
                dq.append((i, j))
            ans = 0 # NOTE
            while dq:
                cnt = len(dq)
                for _ in range(cnt):
                    i, j = dq.popleft()
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] == False:
                            if grid[ni][nj] == 1:
                                return ans # NOTE
                            if grid[ni][nj] == 0:
                                visited[ni][nj] = True
                                dq.append((ni, nj))
                ans += 1

        return bfs()

# @lc code=end

# Inputs
[[0,1],[1,0]]
[[0,1,0],[0,0,0],[0,0,1]]
[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
