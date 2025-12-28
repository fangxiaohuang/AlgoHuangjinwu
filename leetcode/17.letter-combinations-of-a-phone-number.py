#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        
        hmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        s = hmap[digits[0]]
        # 只有1个数字，后面无，无需跟后面的进行拼接直接返回
        if n == 1:
            for c in s:
                ans.append(c)
            return ans
        # 当前数字的结果与后面的进行拼接后返回
        remains = self.letterCombinations(digits[1:])
        for sub_letter in remains:
            for c in s:
                ans.append(c+sub_letter)
        return ans

        
# @lc code=end