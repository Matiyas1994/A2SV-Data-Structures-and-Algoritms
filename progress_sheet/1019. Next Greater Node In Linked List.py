# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:        
        p = head
        arr=[]    
        while p:
            arr.append(p.val)
            p = p.next
            
    
        res = [0]*len(arr)
        
        stack = []
        p = len(arr)-1
        
        while p >= 0:
            while stack and arr[p] >= stack[-1]: 
                stack.pop()
            if stack:
                res[p] = stack[-1] 
            
            stack.append(arr[p])
            p -=1
        return res
            
