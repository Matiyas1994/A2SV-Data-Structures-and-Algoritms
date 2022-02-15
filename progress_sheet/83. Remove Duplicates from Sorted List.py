# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        
        if head.next == None:
            return head
        
        p1 = head
        p2 = p1.next
        
        while p2:
            while  p1.val == p2.val:
                if p2.next == None:
                    p1.next = None
                    return head
                
                p2 = p2.next
            p1.next = p2
            p1 = p2
            p2 = p2.next
            
        return head
