# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None :
            return head
        
        iterater = head
        p1 = head.next
        p2 = head
        while p1:
            if p1.val < p2.val:
                iterater = head
                i2 = head
                while  iterater.val <= p1.val:
                    i2 = iterater
                    iterater = iterater.next
                    
                if iterater == head:
                    p2.next = p1.next
                    p1.next = iterater
                    head = p1
                    p1 = p2.next
                else:
                    p2.next = p1.next
                    p1.next = i2.next
                    i2.next = p1
                    p1 = p2.next
            else:
                p1 = p1.next
                p2 = p2.next
        return head
                
