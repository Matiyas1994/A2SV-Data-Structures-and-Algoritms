# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head.next.next ==None:
            return head.val + head.next.val
        
        leftP = 0
        cur = head
        arr = []
        Max = float(-inf)
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        
        n = len(arr)
        while leftP <= (n / 2) - 1:
            Max = max(Max,arr[leftP] + arr[n-1-leftP])
            leftP +=1
        
        return Max
