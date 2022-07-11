# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        queue = deque()
        
        if root: queue.append([root, 0])
        
        # Use a stack to select the right-most node for each layer
        while queue:
            cur_node, cur_depth = queue.pop()
            if cur_node.left: queue.append([cur_node.left, cur_depth + 1])
            if cur_node.right: queue.append([cur_node.right, cur_depth + 1])
            if cur_depth >= len(right_side_view): right_side_view.append(cur_node.val) 
            
        return right_side_view
