class Solution(object):
    def intToRoman( num):
        """
        :type num: int
        :rtype: str
        """
        output=''
        def calculate(output,Num,mark):
            Symbol1=['M','C','X','I']
            Symbol2=['D','L','V']
            if 0<Num and Num<4:
                output=output+Symbol1[mark]*Num
            elif Num==4:
                output=output+Symbol1[mark]+Symbol2[mark-1]
            elif Num>4 and Num<9:
                output=output+Symbol2[mark-1]+Symbol1[mark]*(Num-5)
            elif Num==9:
                output=output+Symbol1[mark]+Symbol1[mark-1]
            return output
                

        
        Num_q=num//1000 % 10
        if Num_q>0:
            output=calculate(output,Num_q,0)

        Num_b=num//100 % 10
        if Num_b>0:
            output=calculate(output,Num_b,1)
        Num_s=num//10 % 10
        if Num_s>0:
            output=calculate(output,Num_s,2)
        Num_g=num%10
        if Num_g>0:
            output=calculate(output,Num_g,3)

        return  output
s=Solution
s.intToRoman(1994)