# For this solution I overthought it and shouldn't have used the binary search. It would have been a better idea to instead have the second and third index move 
# according to the sum with the third index being a postive number that moves left when the sum is postive and the second pointer moving right when the sum is negative. 
https://leetcode.com/problems/3sum/
Runtime: 7626 ms, faster than 5.13% of Python3 online submissions for 3Sum.
Memory Usage: 18 MB, less than 81.47% of Python3 online submissions for 3Sum.
class Solution:
    def binary_search(self, nums, first_index, second_index, target):
        if first_index > second_index:
            return False
        elif nums[(first_index + second_index)//2] == target:
            return True
        else:
            if target < nums[(first_index + second_index)//2]:
                return self.binary_search(nums, first_index, (first_index + second_index)//2 - 1, target)
            else:
                return self.binary_search(nums, (first_index + second_index)//2 + 1, second_index, target) 
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        if len(nums) < 3: return triplets
        
        nums.sort()
        first_index = 0
        
        while first_index < len(nums) - 2 and nums[first_index] < 0:
            second_index = len(nums) - 1 
            while second_index > 1 and nums[second_index] > 0:
                if -nums[first_index] > nums[second_index] + nums[second_index-1]:
                    break
                while nums[second_index - 1] > -nums[first_index] - nums[first_index + 1]:
                    second_index -= 1  
                    
                if(self.binary_search(nums, first_index + 1, second_index - 1, -nums[first_index] - nums[second_index])):
                    triplets.append([nums[first_index],  nums[second_index], -nums[first_index] - nums[second_index]])
                
                # avoid duplciates
                second_index -= 1 
                while nums[second_index + 1] == nums[second_index]:
                    second_index -= 1
                
            # avoid duplciates
            first_index += 1 
            while first_index < len(nums) and nums[first_index - 1] == nums[first_index]:
                first_index += 1
              
        if first_index + 2 < len(nums) and nums[first_index] ==  nums[first_index + 1]  ==  nums[first_index + 2] == 0:
            triplets.append([0,0,0])
            
        return triplets
