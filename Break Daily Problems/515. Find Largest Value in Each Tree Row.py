# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            maxi = float(-inf)
            for _ in range(n):
                node = queue.popleft()
                if node:
                    maxi = max(node.val,maxi)
                    queue.append(node.left)
                    queue.append(node.right)
                
            ans.append(maxi)
        ans.pop()
        return ans
