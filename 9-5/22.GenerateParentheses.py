from distutils import ccompiler


class Solution(object):
    def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=['()']
        if n==1:
            return result
        
        
        for i in range(n-1):
            result1=[]
            for j in range(len(result[0])):
                for k in range(len(result)):
                    if result[k][0:j+1]+'()'+result[k][j+1:len(result[k])] not in result1:
                        result1.append(result[k][0:j+1]+'()'+result[k][j+1:len(result[k])])
            result=result1
        return result

s=Solution
s.generateParenthesis(3)