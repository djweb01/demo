from gettext import find
from turtle import left


class Solution(object):
    def isMatch( s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        while True:
            num=0
            for i in range(len(p)):
                if p[i]=='.':
                    num+=1
                    if s=='':
                        return False
                elif p[i]=='*':
                    num=num*-1
                    if i==len(p)-1 and s=='' and num==0:
                        return True
                else:
                    letter=p[i]
                    loc=s.find(letter,abs(num),len(s))

                    if loc>-1 and ((num>=0 and loc==num) or (num<0 and loc>=-1*num)):
                        p=p[i+1:] if loc+1<len(p) else ''
                        s=s[loc+1:] if loc+1<len(s) else ''
                        
                        if p=='' and s=='':
                            return True
                        else:
                            break
                    else:
                        return False

            return False


s=Solution
s.isMatch("aa","*a")