# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''''
        c=0
        p=head
        while (head !=None):
            c+=1
            head=head.next
       
        k=-1;
        while k < (c//2)-1:
            p=p.next
            k+=1
        return p
        '''
        pf= head
        ps = head

        while (pf!=None and pf.next!=None):
            pf=pf.next.next
            ps=ps.next
            
        return ps
