# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res =[]
        queue = deque()
        visited = set()
        queue.append(root)
        
        while queue:
            n=len(queue)
            Sum = 0
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                Sum +=node.val
                
            res.append(Sum/n)
        return res
        
       
            
