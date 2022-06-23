#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue, second_queue, output_list = [root], [], [[]]
        
        while len(queue):
            cur_node = queue.pop()
            output_list[-1].append(cur_node.val)
            if cur_node.left: second_queue.insert(0, cur_node.left)
            if cur_node.right: second_queue.insert(0, cur_node.right)
            #print(queue)
            #print(second_queue)
            if not len(queue) and len(second_queue):
                queue.extend(second_queue)
                second_queue.clear()
                output_list.append([])
    
        return output_list
        
        
        
        
