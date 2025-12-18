#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (68.77%)
# Likes:    5356
# Dislikes: 139
# Total Accepted:    388.3K
# Total Submissions: 561.8K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
# 
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
# 
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
# 
# 
# Example 1:
# 
# 
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
# 
# 
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                adj[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        lowcost = [adj[i][0] for i in range(n)] # V-U中的节点i到U的最近距离
        INF = float("inf")
        ans = 0
        for i in range(1, n): # NOTE 找出n-1个顶点
            # 找到下一个代价最小的顶点加入U
            cost = INF
            k = -1
            for j in range(n):
                if lowcost[j] != 0 and lowcost[j] < cost:
                    cost = lowcost[j]
                    k = j
            
            ans += cost
            lowcost[k] = 0

            # 更新其他节点到U的代价
            for j in range(n):
                if lowcost[j] != 0:
                    lowcost[j] = min(lowcost[j], adj[k][j])
        return ans
        
# @lc code=end

