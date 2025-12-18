#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = -1

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
        diff = val - self.min_val
        if diff < 0:
            self.min_val = val
        self.stack.append(diff)
        

    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack[-1] < 0:
            self.min_val -= self.stack[-1]
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_val
        else:
            return self.min_val + self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

