# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
     
        if list1==None:
            return list2
        if list2==None:
            return list1
        
        curr= None
        p1 = list1
        p2 = list2
        
        if p1.val <= p2.val:
            curr = p1
            p1 =p1.next
        else:
            curr = p2
            p2 = p2.next
        
        start = curr
        
        while p1 and p2 :
            if p1.val <= p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        if p2 != None:
            curr.next = p2
        elif p1 != None:
            curr.next = p1
            
            
        return start
        
