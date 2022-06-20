# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root 
        stack_nodes = [[current_node, 0]]
        postion_p = -1
        postion_q = -1
        
        while postion_p == -1 or postion_q == -1:
            current_node, curr_pos = stack_nodes.pop(0)
            
            if current_node.val == p.val:
                postion_p = curr_pos
            elif current_node.val == q.val:
                postion_q = curr_pos
                
            if current_node.left != None:
                stack_nodes.append([current_node.left, curr_pos * 2 + 1])
                
            if current_node.right != None:
                stack_nodes.append([current_node.right, curr_pos  * 2 + 2])
        

        #print(postion_p)
        #print(postion_q)
        
        while postion_p != postion_q:
            if postion_p > postion_q:
                postion_p = (postion_p - 1) // 2
            else:
                postion_q = (postion_q - 1) // 2 
            #print(postion_p)
            #print(postion_q)
        
        current_node = root 
        stack_nodes = [[current_node, 0]]
        
        while True:
            current_node, curr_pos = stack_nodes.pop(0)
            
            if curr_pos == postion_p:
                return current_node
                
            if current_node.left != None:
                stack_nodes.append([current_node.left, curr_pos * 2 + 1])
                
            if current_node.right != None:
                stack_nodes.append([current_node.right, curr_pos  * 2 + 2])

            
        
