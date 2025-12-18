#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (62.71%)
# Likes:    14777
# Dislikes: 759
# Total Accepted:    1.3M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
#
# Follow-up: Can you solve the problem in O(1) extra memory space?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        pre, tail, count = dummy_head, head, 1 # NOTE 当前段的前一个, 当前段的最后一个,当前段的总计数
        while tail:
            if count % k == 0: # 当前长度正好为k
                p = pre.next # 当前段的第1个,也是反转后的最后1个
                for _ in range(k-1): # 依次将第2个到第k个节点加到pre后面
                    q = p.next
                    p.next = q.next
                    q.next = pre.next
                    pre.next = q
                pre = p
                tail = pre.next
            else: # 不够k, tail继续后移
                tail = tail.next
            count += 1 # NOTE if else里面tail都更新了，因此这里可以直接加1
        return dummy_head.next


# @lc code=end

