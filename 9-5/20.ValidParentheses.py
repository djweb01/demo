from fileinput import close


class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        closeC = {'(':')','[':']','{':'}'}
        if s == '':
            return False
        
        for i in s:
            
            if i in closeC and s.count(i) != s.count(closeC[i]):
                return False

        def checkValid(s):
            i=0
            while True:
                if s[i] in closeC:
                    loc=s.find(closeC[s[i]],i+1,len(s))
                    n=s.count(s[i],i+1,loc)
                    if n!=0:
                        while True:
                            loc=s.find(closeC[s[i]],loc+1,len(s))
                            if s.count(s[i],i+1,loc) == s.count(closeC[s[i]],i+1,loc):
                                break

                            
                    if loc!=-1 and (loc-i)%2==1:
                        if loc-i>1:
                            if checkValid(s[i+1:loc]) == False:
                                return False
                        if loc != len(s)-1:
                            i=loc+1
                        else:
                            return True
                    else:
                        return False
                else:
                    return False

            

        if checkValid(s):
            return True
        else:
            return False


s=Solution
s.isValid("[({(())}[()])]")