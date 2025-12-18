#
# @lc app=leetcode id=1383 lang=python3
#
# [1383] Maximum Performance of a Team
#
# https://leetcode.com/problems/maximum-performance-of-a-team/description/
#
# algorithms
# Hard (47.52%)
# Likes:    3168
# Dislikes: 84
# Total Accepted:    104.1K
# Total Submissions: 219K
# Testcase Example:  '6\n[2,10,3,1,5,8]\n[5,4,3,9,7,2]\n2'
#
# You are given two integers n and k and two integer arrays speed and
# efficiency both of length n. There are n engineers numbered from 1 to n.
# speed[i] and efficiency[i] represent the speed and efficiency of the i^th
# engineer respectively.
#
# Choose at most k different engineers out of the n engineers to form a team
# with the maximum performance.
#
# The performance of a team is the sum of its engineers' speeds multiplied by
# the minimum efficiency among its engineers.
#
# Return the maximum performance of this team. Since the answer can be a huge
# number, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation:
# We have the maximum performance of the team by selecting engineer 2 (with
# speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
# That is, performance = (10 + 5) * min(4, 7) = 60.
#
#
# Example 2:
#
#
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# Output: 68
# Explanation:
# This is the same example as the first but k = 3. We can select engineer 1,
# engineer 2 and engineer 5 to get the maximum performance of the team. That
# is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
#
#
# Example 3:
#
#
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# Output: 72
#
#
#
# Constraints:
#
#
# 1 <= k <= n <= 10^5
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 10^5
# 1 <= efficiency[i] <= 10^8
#
#
#

# @lc code=start
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []
        for i in range(n):
            engineers.append((speed[i], efficiency[i]))
        sorted_engineers = sorted(engineers, key=lambda x: x[1], reverse=True)

        min_pq = []
        speed_sum = 0
        ans = 0
        for s, e in sorted_engineers:
            if len(min_pq) >= k:
                speed_min = heapq.heappop(min_pq)
                speed_sum -= speed_min
            heapq.heappush(min_pq, s) # NOTE
            speed_sum += s
            ans = max(ans, speed_sum * e)
        MOD = 10**9 + 7
        return ans % MOD
# @lc code=end

