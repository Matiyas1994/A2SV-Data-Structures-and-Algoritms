# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        temparr=[]
        while curr != None:
            temparr.append(curr.val)
            curr = curr.next
        cdic=Counter(temparr)
        
        arr2=[]
        for key , val in cdic.items():
            if val == 1:
                arr2.append(key)
        arr2.sort()
        
        ans =None
        for data in arr2:
            newNode= ListNode(data)
            if ans:
                cur = ans
                while cur.next != None:
                    cur = cur.next
                cur.next = newNode
            else:
                ans = newNode 

        return ans
        
    

    
    
     
      
        '''
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            temp = head.val
            while head and head.val == temp:
                head = head. next
            if head == None:
                return 
        stack = []
        curr= head
        prev=head
        stack.append(curr)
        curr= curr.next
        
        while curr != None:
            if stack[-1].val == curr.val:
                while curr and curr.val == stack[-1].val:
                    curr = curr.next
                prev.next= curr
                stack.pop()
                stack.append(curr)
            else:
                stack.append(curr)
                prev = stack[-2]
            if curr:
                curr = curr.next
            
        return head
        '''
