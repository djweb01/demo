class Solution(object):
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        a=[len(st) for st in strs]
        if min(a)==0:
            return ""
        if len(a)==1:
            return strs[0]

        b=[x for x in range(len(a))]
        len(strs[0])
        result=strs[a.index(min(a))]
        b.pop(a.index(min(a)))
        for i in range(min(a)):
            if sum(result == strs[x][0:len(result)] for x in b)==len(b):
                return result
            elif len(result)==1:
                return ""
            result=result[0:-1]
            

s=Solution
s.longestCommonPrefix(["flower","flow","flight"])