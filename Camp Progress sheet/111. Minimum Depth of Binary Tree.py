# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
    
        if not root:
            return 0
        return self.find_depth(root, 0)
        
    def find_depth(self, root, depth_counter):
    
        if not root:
            return
        depth_counter += 1
            
        if not root.left and not root.right:
            return depth_counter
                
            
        left = self.find_depth(root.left, depth_counter)
        right = self.find_depth(root.right, depth_counter)
        
        if not left:
            return right
        if not right:
            return left
        return min(left, right)
    
