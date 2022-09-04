#LEEKCOOE exercise 9

class Solution(object):
    def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            y=str(x)
            y2=y[::-1]
            if y==y2:
                return True
            else:
                return False
        else:
            return False

s=Solution
s.isPalindrome(0)