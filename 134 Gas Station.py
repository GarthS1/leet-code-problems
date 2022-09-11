#https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        local_min = 0
        global_min = float('inf')
        start_index = 0
        length = len(gas)
        sum_array = 0
         
        for index in range(2 * length):
            # Caculate the min subarray. It than follows that the starting point must be the point after the end of the min subarray as it is unique
            local_min = min(gas[index % length] - cost[index % length], gas[index % length] - cost[index % length] + local_min)
            sum_array += gas[index % length] - cost[index % length]
            if local_min < global_min:
                global_min = local_min
                start_index = index + 1
        
        return start_index % length if sum_array >= 0 else -1
