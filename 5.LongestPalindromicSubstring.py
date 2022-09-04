from unittest import result


class Solution(object):
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        s_1 = s[::-1]
        st = ''
        i=0
        result=s[0] if len(s)>0 else ''
        while True:
            if len(result)>=len(s):
                break
            st=s[0:i+1]
            if s_1.rfind(st,0,len(s)-1-i)==-1: #no find
                s=s[1:len(s)]
                s_1=s_1[0:len(s_1)-1]
                i=0
            else:
                j=s_1.rfind(st,0,len(s)-1-i)

                while True: 
                    
                    if j-1>=0+i and s_1[j-1:j+i]==st:
                        j-=1
                        continue                   
                    if (j>(i+1) and s_1[j-1-i:j]==st):
                        j=j-1-i
                    else:
                        break

                result=s[0:len(s)-j] if (len(s)-j) > len(result) else result
                i+=1
            
        
        return result

s=Solution
s.longestPalindrome("absdebba")