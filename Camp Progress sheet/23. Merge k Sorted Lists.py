# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        All =[]
        
        if not list:
            return 
        for i in range(len(lists)):
            p = lists[i]        
            while p:
                All.append(p.val)
                p = p.next
        All.sort()
        if not All:
            return
        
        def builder(mylist):
            stack =[]
            for i in range(len(mylist)):
                stack.append(ListNode(mylist[i]))
            
            for i in range(len(stack)-1):
                stack[i].next = stack[i+1]
                
            stack[len(stack)-1].next = None
            
            return stack[0]
        
        return builder(All)        
    
