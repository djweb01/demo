#Runtime: 21 ms, faster than 76.59% 
#Memory Usage: 13.7 MB, less than 15.69% 

class Solution(object):
    def letterCombinations( digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        if digits=='':
            return []
        digits=list(digits)
        result=[list(letter[int(x)]) for x in digits]
        
        if len(digits)>1:
            result0=result[0]
            for k in range(1,len(digits)):
                result0=[i+j for i in result0 for j in result[k]]
            return result0
        else:
            return result[0]



s=Solution
s.letterCombinations('2')