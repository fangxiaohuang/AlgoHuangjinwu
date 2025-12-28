#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (47.48%)
# Likes:    19499
# Dislikes: 768
# Total Accepted:    1.4M
# Total Submissions: 2.9M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
#
# Return the max sliding window.
#
#
# Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#

# @lc code=start
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_pq = []
        ans = []
        for i, num in enumerate(nums):
            # NOTE Ensure the heap top element is within the valid window
            while max_pq and max_pq[0][1] < i - k + 1:
                heapq.heappop(max_pq)
            heapq.heappush(max_pq, (-num, i))
            if i >= k-1:
                ans.append(-max_pq[0][0])
        return ans
# @lc code=end

