# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        new_head = dummy_head = head
        while head:
            size+=1
            head = head.next
        stop = size - n
        if stop == 0: return new_head.next
        counter = 1
        while dummy_head:
            if counter == stop:
                dummy_head.next = dummy_head.next.next
                return new_head
            counter+=1
            dummy_head = dummy_head.next
    
        

s=Solution
s.removeNthFromEnd([1,2,3,4,5],2)