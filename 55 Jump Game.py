# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        if len(nums) == 1:
            return True 
        
        # Can reach the end of the array from anywhere in the array 
        can_reach_end = False
        for i in range(len(nums) - 1, -1, -1):
            if len(nums) - 1 <= nums[i] + i:
                can_reach_end = True
                break
        
        if not can_reach_end:
            return False
        
        current_zero_index = -1
        
        # Can get past any zero in the array 
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0 and current_zero_index == -1:
                current_zero_index = i
            elif current_zero_index < nums[i] + i:
                current_zero_index = -1
            
        if current_zero_index != -1:    
            return False
        
        return True 
        
