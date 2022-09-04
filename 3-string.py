from operator import index
from turtle import Turtle


class Solution(object):
    def lengthOfLongestSubstring(s):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        ans = 0
        sub = ''
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return ans

s=Solution
s.lengthOfLongestSubstring("au")