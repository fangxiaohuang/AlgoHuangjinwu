#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.size = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.size < self.max_size:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if not self.stack:
            return -1
        val = self.stack.pop()
        self.size -= 1
        return val

    def increment(self, k: int, val: int) -> None:
        k = min(k, self.size)
        tmp_stack = []
        for i in range(self.size - k):
            tmp_stack.append(self.stack.pop())
        for _ in range(k):
            tmp_stack.append(self.stack.pop() + val)
        while tmp_stack:
            self.stack.append(tmp_stack.pop())
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

