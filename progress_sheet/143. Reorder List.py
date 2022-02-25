# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        deQ= deque([])
        p = head
        
        while p != None:
            deQ.append(p)
            p = p.next
        
        while deQ:
            t = deQ.pop()
            if deQ:
                b = deQ.popleft()
                b.next = t
            else:
                t.next = None 
            if deQ:
                t.next = deQ[0]
            else:
                t.next = None
            
            
