# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    # Function to find the max subarray in array given the indexs
    def findMaxSubarray(self, first_index, second_index, current_sum, nums) -> int:
        if first_index >= second_index:
            return nums[second_index]
        elif current_sum > 0:
            return current_sum
        
        # Find the min product needed to convert the current_sum to a postive number 
        first_negative_product = 1
        second_negative_product = 1
        
        while True:
            if nums[first_index] < 0:
                first_negative_product *= nums[first_index]
                break
            else: 
                first_negative_product *= nums[first_index]
                first_index += 1
                
        while True:
            if nums[second_index] < 0:
                second_negative_product *= nums[second_index]
                break
            else: 
                second_negative_product *= nums[second_index]
                second_index -= 1   
        
        return max(current_sum // first_negative_product, current_sum // second_negative_product)
        
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        global_max, current_max, first_index = float('-inf'), 1, 0
        
        # Use something similar to Kadane's Algorithm where we multiply until we hit either a zero or the end of the array 
        for i in range(len(nums)):
            if nums[i] == 0:
                global_max = max(global_max, 0, self.findMaxSubarray(first_index, i - 1, current_max, nums))
                first_index = i + 1
                current_max = 1
            else: 
                current_max *= nums[i]    
        
        return max(global_max, self.findMaxSubarray(first_index, len(nums) - 1, current_max, nums))
        
