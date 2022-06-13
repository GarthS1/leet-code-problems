https://leetcode.com/problems/container-with-most-water/
Runtime: 792 ms	
Memory: 27.4 MB
  
class Solution:
    def maxArea(self, height: List[int]) -> int:
        first_pointer = 0
        second_pointer  = len(height) - 1
        max_volume = min(height[first_pointer], height[second_pointer]) * (second_pointer - first_pointer)
        
        while first_pointer != second_pointer:
            if height[first_pointer] <=  height[second_pointer]:
                first_pointer += 1
                if max_volume <  min(height[first_pointer], height[second_pointer]) * (second_pointer - first_pointer):
                    max_volume = min(height[first_pointer], height[second_pointer]) * (second_pointer - first_pointer)
            else:
                second_pointer -= 1
                if max_volume <  min(height[first_pointer], height[second_pointer]) * (second_pointer - first_pointer):
                    max_volume = min(height[first_pointer], height[second_pointer]) * (second_pointer - first_pointer)
            
        return max_volume
