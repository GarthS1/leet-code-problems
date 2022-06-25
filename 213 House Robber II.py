# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helperRob(nums[1:]), self.helperRob(nums[:-1]))
    
    def helperRob(self, nums: List[int]) -> int:
        cur, t_0 = 0, nums[0]
        
        t_1 = nums[1] if len(nums) > 1 else 0
        t_2 = nums[2] + t_0 if len(nums) > 2 else 0
        
        for i in range(3, len(nums)):
            cur = nums[i] + max(t_0,t_1)
            t_0, t_1, t_2 = t_1, t_2, cur
    
        return max(t_0,t_1,t_2)
        
