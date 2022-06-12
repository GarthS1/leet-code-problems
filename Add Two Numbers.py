https://leetcode.com/problems/add-two-numbers/
Runtime: 78 ms
Memory Usage: 14 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num = ""
        second_num = ""
        
        while l1 is not None:
            first_num  += str(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            second_num += str(l2.val)
            l2 = l2.next
    
        total_num = int(first_num[::-1]) + int(second_num[::-1])
        length_num = len(str(total_num))
        total_num_list_head = ListNode(total_num % 10)
        total_num =  total_num // 10
        total_num_list = total_num_list_head
        
        for i in range(length_num - 1):
            total_num_list.next = ListNode()
            total_num_list = total_num_list.next
            total_num_list.val = total_num % 10
            total_num =  total_num // 10
            
        return total_num_list_head
