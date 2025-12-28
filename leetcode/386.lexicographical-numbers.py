#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (73.09%)
# Likes:    3099
# Dislikes: 214
# Total Accepted:    376K
# Total Submissions: 493.8K
# Testcase Example:  '13'
#
# Given an integer n, return all the numbers in the range [1, n] sorted in
# lexicographical order.
#
# You must write an algorithm that runs in O(n) time and uses O(1) extra
# space. 
#
#
# Example 1:
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:
# Input: n = 2
# Output: [1,2]
#
#
# Constraints:
#
#
# 1 <= n <= 5 * 10^4
#
#
#

# @lc code=start

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(num):
            ans.append(num)
            for i in range(10):
                nnum = num*10 + i
                if nnum <= n:
                    dfs(nnum)

        for i in range(1, 10):
            dfs(i)

        return ans


# @lc code=end

