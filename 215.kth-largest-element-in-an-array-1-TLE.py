#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (67.84%)
# Likes:    18147
# Dislikes: 948
# Total Accepted:    3.2M
# Total Submissions: 4.6M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
# Can you solve it without sorting?
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left, right):
            pivot_idx = random.randint(left, right)
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            # pivot = nums[i]
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def find(left, right, k):
            i = partition(left, right)
            left_len = i - left + 1
            if left_len == k:
                return nums[i]
            elif left_len > k:
                return find(left, i-1, k)
            else:
                return find(i+1, right, k - (left_len)) # NOTE

        return find(0, len(nums)-1, k)
# @lc code=end

