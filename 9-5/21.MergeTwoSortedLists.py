# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from turtle import Turtle


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1!=None:
            return list2
        
        if list2!=None:
            return list1

        if list1.val<=list2.val:
            result=sta=ListNode(list1.val)
            list1=list1.next
            
        else:
            result=sta=ListNode(list2.val)
            list2=list2.next
            


        while True:
            if (list1!=None and list2!=None and list1.val<=list2.val) or (list1!=None and list2==None):
                result.next=ListNode(list1.val)
                list1=list1.next   
            elif (list1!=None and list2!=None) or (list1==None and list2!=None):
                result.next=ListNode(list2.val)
                list2=list2.next   
            else :
                return sta
            result=result.next
            

            
            
            
            
            
s=Solution
s.mergeTwoLists([1,2,4],[1,3,4])