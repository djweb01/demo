class Solution(object):
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        y=x if x>=0 else -1*x
        result=str(y)
        result=result[::-1]
        result=int(result) if x>=0 else -1*int(result)
        

        return result




s=Solution
s.reverse(0)