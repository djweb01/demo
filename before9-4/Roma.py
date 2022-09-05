class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        output=''
        def calculate(output,mark):
            Symbol1=['M','C','X','I']
            Symbol2=['D','L','V']
            if 0<Num_q and Num_q<4:
                output=output+Symbol1[mark+1]*Num_q
            elif Num_q==4:
                output=output+Symbol1[mark+1]+Symbol2[mark]
            elif Num_q>4 and Num_q<9:
                output=output+Symbol2[mark]+Symbol1[mark+1]*Num_q
            elif Num_q==9:
                output=output+Symbol1[mark+1]+Symbol1[mark]
            return output
                

        if s.isdigit(s)==False:
            print('This is not a value')
            return
        elif s%1 >0:
            
            print('This value is a float, which is out of range')
            return
        
        Num_q=s//1000 % 10
        
        if Num_q>1:
            print('This valus is out of range')
            return
        else:
            output=output+'M'
        
        Num_b=s//100 % 10
        output=calculate(output,0)
        Num_s=s//10 % 10
        output=calculate(output,1)
        Num_g=s%10
        output=calculate(output,2)
        print('Roman numerals')
        return

S=Solution
S.romanToInt(10)