#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (63.00%)
# Likes:    9887
# Dislikes: 1047
# Total Accepted:    624.2K
# Total Submissions: 985.4K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
#   '[2.0,3.0]\n' +
#   '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
# equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
# single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the
# j^th query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.
#
# Note: The variables that do not occur in the list of equations are undefined,
# so the answer cannot be determined for them.
#
#
# Example 1:
#
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
#
# Example 2:
#
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
#
#
# Example 3:
#
#
# Input: equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
#
# Constraints:
#
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
#
#
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            ori_parent = self.parent[x] # NOTE Save original parent
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[ori_parent]
        return self.parent[x]

    def union(self, x, y, val):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        # NOTE no need to use rank, since only x to y
        self.parent[rootx] = rooty
        self.weight[rootx] = val * self.weight[y] / self.weight[x]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # char to index
        char2idx = {}
        idx = 0
        for e in equations:
            if e[0] not in char2idx:
                char2idx[e[0]] = idx
                idx += 1
            if e[1] not in char2idx:
                char2idx[e[1]] = idx
                idx += 1

        UF = UnionFind(idx+1)
        for i, (c1, c2) in enumerate(equations):
            x, y = char2idx[c1], char2idx[c2]
            UF.union(x, y, values[i])

        ans = []
        for c1, c2 in queries:
            x, y = char2idx.get(c1, None), char2idx.get(c2, None)
            if x is None or y is None:
                ans.append(-1.0)
                continue
            rootx, rooty = UF.find(x), UF.find(y)
            if rootx == rooty:
                ans.append(UF.weight[x] / UF.weight[y]) # NOTE it's x/y, nt rootx/rooty
            else:
                ans.append(-1.0)
        return ans



# @lc code=end

