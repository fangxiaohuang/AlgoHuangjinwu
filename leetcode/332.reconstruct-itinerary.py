#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Hard (43.53%)
# Likes:    6193
# Dislikes: 1914
# Total Accepted:    508.8K
# Total Submissions: 1.2M
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight. Reconstruct
# the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK", thus, the
# itinerary must begin with "JFK". If there are multiple valid itineraries, you
# should return the itinerary that has the smallest lexical order when read as
# a single string.
#
#
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
# ["JFK", "LGB"].
#
#
# You may assume all tickets form at least one valid itinerary. You must use
# all the tickets once and only once.
#
#
# Example 1:
#
#
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
#
#
# Example 2:
#
#
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
#
#
#
# Constraints:
#
#
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi
#
#
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)

        for v in graph.values():
            v.sort(reverse=True) # NOTE list.pop() O(1), list.pop(1) O(n)


        ans = []
        def dfs(u):
            while len(graph[u]) > 0:
                v = graph.[u].pop()
                dfs(v)
            ans.append(u)

        dfs("JFK")
        return ans[::-1]



# @lc code=end

