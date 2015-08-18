#边界0值1.None 2.len == 0；临界值光想不如找特例；不畏平方复杂度；归一化
"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if s == None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        i = 0
        j = 1
        longest = 1
        while j < len(s):
            tmp = j - i
            if s[j] in s[i:j]:
               # print s[i:j].index(s[j])
                i = s[i:j].index(s[j]) + i + 1
            else:
                tmp = tmp + 1
            if tmp > longest:
                longest = tmp
            j = j + 1

        print longest
        return longest

Solution().lengthOfLongestSubstring("bbbabcd")
