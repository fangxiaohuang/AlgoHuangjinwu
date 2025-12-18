#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (87.43%)
# Likes:    7154
# Dislikes: 387
# Total Accepted:    1.3M
# Total Submissions: 1.5M
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range
# [low, high].
#
#
# Example 1:
#
#
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 =
# 32.
#
#
# Example 2:
#
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 =
# 23.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 2 * 10^4].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Generate the complete inorder in advance
        inorder = []
        p, stack = root, [] # 指向当前待处理的节点, 存储暂不处理的节点
        while stack or p is not None:
            # First: left
            while p: # NOTE
                stack.append(p)
                p = p.left
            # Second: update p to root and record value
            p = stack.pop()
            inorder.append(p.val)
            # NOTE Third: update p to right
            p = p.right

        i = 0
        while inorder[i] < low:
            i += 1
        ans = 0
        while i < len(inorder) and inorder[i] <= high:
            ans += inorder[i]
            i += 1
        return ans

# @lc code=end

