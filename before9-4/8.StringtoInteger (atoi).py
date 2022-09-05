class Solution(object):
    def myAtoi(s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        if s=='':
            return 0
        result=''
        sin=1
        
        l=list(map(list,s))
        for i in range(len(l)):
            if s[i].isdigit() or (i==0 and (s[0]=='+' or s[0]=='-')):
                if s[i].isdigit()==False:
                    if len(l)==1:
                        return 0
                    sin=-1 if s[0]=='-' else sin
                    continue
                
                result+=s[i]
                if i+1<len(l) and s[i+1].isdigit():
                    continue
                
                result=int(result)*sin
                if result<-2**31:
                    result=-2**31
                elif result>2**31-1:
                    result=2**31-1
                break
            else:
                result=0
                break
        return result
s=Solution
s.myAtoi("+")