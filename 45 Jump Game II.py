# https://leetcode.com/problems/jump-game-ii/
class Solution:      
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        jumps = 0
        current_index = len(nums) - 1
        
        # Find max jump you can make starting at the end of the array
        while current_index > 0:
            current_jump = 0
            current_jump_index = 0
            
            for i in range(current_index - 1, -1, -1):
                if current_jump <= i + nums[i]:
                    current_jump =  min(i + nums[i], current_index) # Need this to not overjump
                    current_jump_index = i

            current_index = current_jump_index
            jumps += 1

        return jumps
        
