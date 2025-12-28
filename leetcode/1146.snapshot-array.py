#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#
# https://leetcode.com/problems/snapshot-array/description/
#
# algorithms
# Medium (36.66%)
# Likes:    3891
# Dislikes: 536
# Total Accepted:    266.8K
# Total Submissions: 727.6K
# Testcase Example:  '["SnapshotArray","set","snap","set","get"]\n[[3],[0,5],[],[0,6],[0,0]]'
#
# Implement a SnapshotArray that supports the following interface:
# 
# 
# SnapshotArray(int length) initializes an array-like data structure with the
# given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to
# val.
# int snap() takes a snapshot of the array and returns the snap_id: the total
# number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we
# took the snapshot with the given snap_id
# 
# 
# 
# Example 1:
# 
# 
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return
# 5
# 
# 
# Constraints:
# 
# 
# 1 <= length <= 5 * 10^4
# 0 <= index < length
# 0 <= val <= 10^9
# 0 <= snap_id < (the total number of times we call snap())
# At most 5 * 10^4 calls will be made to set, snap, and get.
# 
# 
#

# @lc code=start
import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0 # 初始为第0轮snap

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][-1] = (self.snap_id, val) # 正在当前snap_id的turn，直接更新
        else:
            self.arr[index].append((self.snap_id, val)) # 加入新的snap_id

    def snap(self) -> int:
        self.snap_id += 1 # 开启新一轮snap
        return self.snap_id - 1 # 封版当前次snap
        

    def get(self, index: int, snap_id: int) -> int:
        hist = self.arr[index]
        # NOTE 因为hist存的是二维tuple，后面加float("inf")是为了确保按snap_id排序查找第一个大于snap_id的位置
        idx = bisect.bisect_right(hist, (snap_id, float("inf")))
        return hist[idx-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

