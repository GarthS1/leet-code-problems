# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        index, total_time = 0, 0
        
        while index < len(neededTime) - 1:
            if colors[index] != colors[index + 1]:
                index += 1
            else:
                max_time, combined_times = neededTime[index], neededTime[index]
                
                while index < len(neededTime) - 1 and colors[index] == colors[index + 1]:
                    max_time = max(max_time, neededTime[index + 1])
                    combined_times += neededTime[index + 1]
                    index += 1
            
                total_time += combined_times - max_time 
                
        return total_time
