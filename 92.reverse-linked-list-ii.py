#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy_h = ListNode(-1)
        dummy_h.next = head
        pre = dummy_h
        for _ in range(left-1):
            pre = pre.next
        p = pre.next
        q = p.next
        for _ in range(right - left):
            tmp = q.next
            q.next = pre.next
            pre.next = q
            q = tmp
        p.next = q
        return dummy_h.next


        
# @lc code=end

        