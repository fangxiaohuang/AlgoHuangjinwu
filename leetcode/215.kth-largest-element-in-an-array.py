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
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition_double(low, high):
            mid = (low + high) >> 1
            pivot = nums[mid]
            while low <= high:
                while low <= high and nums[low] > pivot:
                    low += 1
                while low <= high and nums[high] < pivot:
                    high -= 1
                if low <= high:
                    nums[low], nums[high] = nums[high], nums[low]
                    low += 1
                    high -= 1
            return high, low

        def find(low, high, k):
            i, j = partition_double(low, high)
            if low + k - 1 <= i:
                return find(low, i, k)
            elif low + k - 1 >= j:
                return find(i+1, right, k - (j-low))
            else:
                return nums[i+1]

        return find(0, len(nums)-1, k)


# @lc code=end
