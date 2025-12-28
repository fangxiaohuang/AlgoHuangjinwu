#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (62.14%)
# Likes:    6210
# Dislikes: 700
# Total Accepted:    359K
# Total Submissions: 576.1K
# Testcase Example:  '[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]'
#
# On a 2D plane, we place n stones at some integer coordinate points. Each
# coordinate point may have at most one stone.
#
# A stone can be removed if it shares either the same row or the same column as
# another stone that has not been removed.
#
# Given an array stones of length n where stones[i] = [xi, yi] represents the
# location of the i^th stone, return the largest possible number of stones that
# can be removed.
#
#
# Example 1:
#
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with
# another stone still on the plane.
#
#
# Example 2:
#
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column
# with another stone still on the plane.
#
#
# Example 3:
#
#
# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove
# it.
#
#
#
# Constraints:
#
#
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10^4
# No two stones are at the same coordinate point.
#
#
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parent = [None] * n
        self.rank = [None] * n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        if self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        else:
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.parent[rooty] = rootx

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        MAXN = 10001
        uf = UnionFind(2*MAXN)
        for i, j in stones:
            uf.union(i, MAXN + j)
        
        # Count the number of unique roots
        # Each unique root represents a connected component
        sets = set()
        for i, _ in stones:
            sets.add(uf.find(i))

        # The number of stones that can be removed is total stones - number of unique roots
        return len(stones) - len(sets)
# @lc code=end

