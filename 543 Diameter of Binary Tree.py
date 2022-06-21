# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_depth = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:       
        self.find_node(root)
        return self.max_depth
    
    def find_node(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        
        left_subtree = self.find_node(root.left)
        right_subtree = self.find_node(root.right)
        
        temp_max_depth = 0
        
        if root.left and root.right:
            temp_max_depth = 2 + left_subtree + right_subtree
        else:
            temp_max_depth = 1 + left_subtree + right_subtree
        
        if temp_max_depth > self.max_depth:
            self.max_depth = temp_max_depth
        
        return 1 + max(left_subtree, right_subtree)
