from copy import copy
from optparse import Values


class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        left=0
        right=len(height)-1
        if right<1:
            return 0
        elif right==1:
            return min(height[0],height[1])
        dist=right-left
        result=min(height[left],height[right])*dist
        while True:
            if right-left==1:
                return result
            dist=right-left
            c=height[left+1:right]
            if height[left]<=height[right]:
                for x in c:
                    c1=left
                    if min(x,height[right]) > result /(dist-1-c.index(x)):
                        c1=c.index(x)+left+1
                        break    
                if c1!=left:
                    left=c1
                    result=min(height[left],height[right])*(right-left)
                else:
                    c=c[::-1]
                    c1=list(map(lambda x: x-result /(dist-1-c.index(x)) , c))
                    c2=list(map(lambda x: x - result /(dist-1-c.index(x)) , c))
                    if max(c1)>0:
                        
                        c2.sort()
                        if c2[-2]>0 and c1.index(c2[-1])  > c1.index(c2[-2]):
                            right=right-1-c1.index(c2[-2])
                        else:
                            right=right-1-c1.index(max(c1)) 
                        
                    else:
                        return result

            else:
                c=c[::-1]
                for x in c:
                    c1=right
                    if min(x,height[left]) > result /(dist-1-c.index(x)):
                        c1=right-1-c.index(x)
                        break  
                if c1!=right:
                    right=c1
                    result=min(height[left],height[right])*(right-left)
                else:
                    c=c[::-1]
                    c1=list(map(lambda x: x - result /(dist-1-c.index(x)) , c))
                    c2=list(map(lambda x: x - result /(dist-1-c.index(x)) , c))

                    if max(c1)>0:
                        
                        c2.sort()
                        if c2[-2]>0 and c1.index(c2[-1])  > c1.index(c2[-2]):
                            left=c1.index(c2[-2])+left+1
                        else:
                            left=c1.index(max(c1))+left+1
                        
                    else:
                        return result

s=Solution
s.maxArea([1,0,0,0,0,0,0,2,2])