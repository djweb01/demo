class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    




class Solution(object):
    
    def addTwoNumbers( l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        r1=[[]]
        while l1:
            r1.append(l1.val)
            l1 = l1.next
        r2=[[]]
        while l2:
            r2.append(l2.val)
            l2 = l2.next


        c=[[]]
        r1=[0]*(max(len(r1),len(r2))-len(r1))+r1
        r2=[0]*(max(len(r1),len(r2))-len(r2))+r2
        for i in range(len(r1)-1,-1,-1):
            c[0].append((r1[i]+r2[i])%10)
            if i == 0 and (r1[i]+r2[i])//10%10>0:
                c[0].append(1)
            elif (r1[i]+r2[i])//10%10>0:
                r1[i-1]+=(r1[i]+r2[i])//10%10

        return c

S=Solution
def add(l):
    for i in range(len(l)):
        self.val=l[i]
        if i<len(l)-1:
            self.next=l[i+1]
    return l 

l1=ListNode.add([9,9,9,9,9,9,9])
l1.add([9,9,9,9,9,9,9])

l2=ListNode
l2.add([9,9,9,9,9])

S.addTwoNumbers(l1,l2)