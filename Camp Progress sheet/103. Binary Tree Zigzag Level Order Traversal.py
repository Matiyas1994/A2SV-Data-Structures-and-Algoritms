# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        queue = deque()
        queue.append(root)
        
        level = 0
        while queue:            
            lenQ= len(queue)
            temp = []
            for _ in range(lenQ):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            level +=1
            if level %2 ==0:
                temp = temp[::-1]
            if temp:
                res.append(temp)
          
        return res
                
        
