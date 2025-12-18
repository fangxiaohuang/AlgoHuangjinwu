#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (68.34%)
# Likes:    3051
# Dislikes: 219
# Total Accepted:    302.6K
# Total Submissions: 442.3K
# Testcase Example:  '["cat","bat","rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other word to form another longer word - let's call this word derivative. For
# example, when the root "help" is followed by the word "ful", we can form a
# derivative "helpful".
# 
# Given a dictionary consisting of many roots and a sentence consisting of
# words separated by spaces, replace all the derivatives in the sentence with
# the root forming it. If a derivative can be replaced by more than one root,
# replace it with the root that has the shortest length.
# 
# Return the sentence after the replacement.
# 
# 
# Example 1:
# 
# 
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled
# by the battery"
# Output: "the cat was rat by the bat"
# 
# 
# Example 2:
# 
# 
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 10^6
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one
# space.
# sentence does not have leading or trailing spaces.
# 
# 
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
# @lc code=end

