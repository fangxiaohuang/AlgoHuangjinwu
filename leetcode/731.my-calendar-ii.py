#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#
# https://leetcode.com/problems/my-calendar-ii/description/
#
# algorithms
# Medium (62.27%)
# Likes:    2237
# Dislikes: 186
# Total Accepted:    203.8K
# Total Submissions: 325.7K
# Testcase Example:  '["MyCalendarTwo","book","book","book","book","book","book"]\n' +
  '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a triple booking.
#
# A triple booking happens when three events have some non-empty intersection
# (i.e., some moment is common to all the three events.).
#
# The event can be represented as a pair of integers startTime and endTime that
# represents a booking on the half-open interval [startTime, endTime), the
# range of real numbers x such that startTime <= x < endTime.
#
# Implement the MyCalendarTwo class:
#
#
# MyCalendarTwo() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be
# added to the calendar successfully without causing a triple booking.
# Otherwise, return false and do not add the event to the calendar.
#
#
#
# Example 1:
#
#
# Input
# ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, true, true, true, false, true, true]
#
# Explanation
# MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
# myCalendarTwo.book(10, 20); // return True, The event can be booked.
# myCalendarTwo.book(50, 60); // return True, The event can be booked.
# myCalendarTwo.book(10, 40); // return True, The event can be double booked.
# myCalendarTwo.book(5, 15);  // return False, The event cannot be booked,
# because it would result in a triple booking.
# myCalendarTwo.book(5, 10); // return True, The event can be booked, as it
# does not use time 10 which is already double booked.
# myCalendarTwo.book(25, 55); // return True, The event can be booked, as the
# time in [25, 40) will be double booked with the third event, the time [40,
# 50) will be single booked, and the time [50, 55) will be double booked with
# the second event.
#
#
#
# Constraints:
#
#
# 0 <= start < end <= 10^9
# At most 1000 calls will be made to book.
#
#
#

# @lc code=start

from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.timeline = defaultdict(int)


    def book(self, startTime: int, endTime: int) -> bool:
        # Add optimistically
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1

        active_events = 0
        sorted_keys = sorted(self.timeline.keys())
        for k in sorted_keys:
            active_events += self.timeline[k]
            if active_events > 2:
                # Rollout
                self.timeline[startTime] -= 1
                self.timeline[endTime] += 1

                # NOTE optimize the subsequent memory usage and lookup efficiency
                if self.timeline[startTime] == 0:
                    del self.timeline[startTime]
                if self.timeline[endTime] == 0:
                    del self.timeline[endTime]

                return False

        return True




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

