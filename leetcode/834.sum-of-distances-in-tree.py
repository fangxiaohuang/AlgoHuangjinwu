#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#
# https://leetcode.com/problems/sum-of-distances-in-tree/description/
#
# algorithms
# Hard (65.30%)
# Likes:    5766
# Dislikes: 139
# Total Accepted:    170.2K
# Total Submissions: 260.4K
# Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
#
# There is an undirected connected tree with n nodes labeled from 0 to n - 1
# and n - 1 edges.
# 
# You are given the integer n and the array edges where edges[i] = [ai, bi]
# indicates that there is an edge between nodes ai and bi in the tree.
# 
# Return an array answer of length n where answer[i] is the sum of the
# distances between the i^th node in the tree and all other nodes.
# 
# 
# Example 1:
# 
# 
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
# 
# 
# Example 2:
# 
# 
# Input: n = 1, edges = []
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.
# 
# 
#

# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        answer = [0] * n
        dp = [0] * n # 以root为根的所有子节点到root的距离之和
        cnt = [0] * n # 以root为根的子树的节点个数
        adj = [[] for _ in range(n)] # [[]]*n为一个空列表的n次引用，所有元素指向同一个内存地址
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        # 求当前root的dp和cnt
        def dfs(root, pre):
            cnt[root] = 1 # 先加上root节点自身
            for v in adj[root]:
                if v == pre:
                    continue
                dfs(v, root)
                dp[root] += dp[v] + cnt[v]
                cnt[root] += cnt[v]

        # 换根逐步求answer
        def dfs_swap(root, pre):
            answer[root] = dp[root]
            for v in adj[root]:
                if v == pre:
                    continue
                # NOTE 记录root和v的原始值，为交换root 和 v求解后的恢复做准备
                dpr, dpv = dp[root], dp[v]
                cntr, cntv = cnt[root], cnt[v]
                # 从root减去v的贡献
                dp[root] -= dp[v] + cnt[v]
                cnt[root] -= cnt[v]
                # 将root作为贡献加到v
                dp[v] += dp[root] + cnt[root]
                cnt[v] += cnt[root]
                dfs_swap(v, root)
                # NOTE 回溯恢复，后面继续求当前root和其他子节点的结果
                dp[root], dp[v] = dpr, dpv
                cnt[root], cnt[v] = cntr, cntv
        
        dfs(0, -1)
        dfs_swap(0, -1)
        return answer
        
# @lc code=end

