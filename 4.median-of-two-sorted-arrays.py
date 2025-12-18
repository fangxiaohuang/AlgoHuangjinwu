#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (43.51%)
# Likes:    30693
# Dislikes: 3449
# Total Accepted:    3.6M
# Total Submissions: 8.1M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        INF = 10**6 + 5
        m, n = len(nums1), len(nums2)

        def findk(nums1, nums2, k):
            m, n = len(nums1), len(nums2)
            i, j = 0, 0
            while k > 1:
                half = k // 2
                i1 = i + half - 1
                vi = nums1[i1] if i1 < m else INF
                j1 = j + half - 1
                vj = nums2[j1] if j1 < n else INF
                if vi < vj:
                    i += half
                else:
                    j += half
                k -= half
            if i >= m:
                return nums2[j]
            if j >= n:
                return nums1[i]
            return minx(nums1[i], nums2[j])

        total = m + n
        k = total//2
        if total % 2 == 1:
            return findk(nums1, nums2, k+1)
        else:
            mid1 = findk(nums1, nums2, k)
            mid2 = findk(nums1, nums2, k+1)
            return (mid1 + mid2) / 2



# @lc code=end

