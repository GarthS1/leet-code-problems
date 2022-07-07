# https://leetcode.com/problems/arithmetic-slices/
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        arithmetic_subarrays = 0
        length_counter = 2
        
        for index in range(2, len(nums)):
            if nums[index - 1] - nums[index - 2] != nums[index] - nums[index - 1]:
                # Comes from the fact that a arithmetic subarray of length 3 has 1 arithmetic subarrays in it, 
                # a arithmetic subarray of length 4 has 3 arithmetic subarrays in it(2 + 1)
                # a arithmetic subarray of length 5 has 6 arithmetic subarrays in it(3 + 2 + 1)
                for i in range(length_counter - 1): arithmetic_subarrays += i 
                length_counter = 2
            else:
                length_counter += 1
        
        for i in range(length_counter - 1): arithmetic_subarrays += i 
                
        return arithmetic_subarrays
