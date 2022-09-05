#寻找字符串 最长公共部分
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
        for i in range(int(min(a)/2+1)):
            b.pop(a.index(min(a)))
            
            if result in (strs[x] for x in b):
                return result
            

           
            if len(result)>2:
                if sum(result[1:len(result)] in strs[x] for x in b)==len(b):
                    return result[1:len(result)]
                elif sum(result[0:-1] in strs[x] for x in b)==len(b):
                    print(result[0:-1])
                    return result[0:-1]
                elif sum(result[0:-2] in strs[x] for x in b)==len(b):
                    return result[0:-2]
                elif sum(result[2:len(result)] in strs[x] for x in b)==len(b):
                    return result[2:-1]
                result=result[1:-1]
            else:
                r=strs[a.index(min(a))]
                for j in r:
                    if sum(j in strs[x] for x in b)==len(b):
                        return j
                    if j == r[-1]:
                        return ""
            

s=Solution
s.longestCommonPrefix(["a"])