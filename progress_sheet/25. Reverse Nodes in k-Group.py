# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return
        stack = deque()
        p= head
        
        while p != None:
            stack.append(p)
            p = p.next
       
        
        head = stack[k-1]
        s2=[]
        
        
        while stack and len(stack) >= k:
            c=0
            while stack and c < k:
                s2.append(stack.popleft())
                c +=1

            while s2 and len(s2) > 1:
                t1=s2.pop()
                t1.next= s2[-1]
        
        
            if stack and len(stack) >= k:
                t2 =s2.pop()
                t2.next = stack[k-1]
        
        
            elif stack and len(stack) < k:
                t3 =s2.pop() 
                t3.next = stack[0]
                
            else:
                t4 =s2.pop()
                t4.next = None
                
        if stack:
            stack[-1].next=None
        
       
        return head

                
    
