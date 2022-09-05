
from unittest import result
class Solution(object):
    def convert( s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result=''
        if numRows<2:
            return s
        a=int(len(s)/(2*numRows-2))+(len(s)%(2*numRows-2))
        for i in range(numRows):
            for j in range(a):         
                result=result+s[i+j*(2*numRows-2)] if (i+j*(2*numRows-2))<len(s) else result
                if i !=0 and i != numRows-1:
                    result=result+s[(j+1)*(2*numRows-2)-i] if ((j+1)*(2*numRows-2)-i)<len(s) else result
  
        return result

s=Solution
s.convert("PAYPALISHIRING",3)