# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return 
        if head.next ==None:
            return head
        p = head
        deq = deque([])
        
        while p != None:
            deq.append(p)
            p = p.next
        
        head = deq[1]
        
        while deq:
            first = deq.popleft()
            second = deq.popleft()
            
            second.next = first
            
            if deq:
                if len(deq)==1:
                    first.next = deq.pop()
                else:
                    first.next = deq[1]
            else:
                first.next = None
            
        return head
        
        
        
        
        
        ''''
        p1 = head
        p2 = head.next
        head = p2
    
        while p2 and p1:
            temp = p2.next
            p2.next = p1
            p1.next = temp
            p1 = p1.next
            p2 = p1.next
        
        return head
        '''
