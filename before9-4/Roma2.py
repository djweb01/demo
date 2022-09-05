class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        output = 0
        for i in range(len(s)):
            symbol=roman[s[len(s)-i-1]]
            if output > symbol*4:
                output = output-symbol
            else:
                output=output+symbol
        return output
            
s=Solution
s.romanToInt('III')