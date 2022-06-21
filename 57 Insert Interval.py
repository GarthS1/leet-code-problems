# First Attempt
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        to_merge = []
        
        # Find ranges to merge 
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            if intervals[index][1] >= newInterval[0]:
                to_merge.append([intervals[index], index])
            index += 1
        
        #print(to_merge)
        if len(to_merge) == 0:
            intervals.insert(index, newInterval)
        else:
            range_insert = [min(to_merge[0][0][0], newInterval[0]), max(to_merge[-1][0][1], newInterval[1])]
            index_to_insert = to_merge[0][1]
            for x in to_merge:
                intervals.remove(x[0])
            intervals.insert(index_to_insert, range_insert)
            
        return intervals   

# Second Attempt
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        first_number = newInterval[0]
        second_number = newInterval[1]
        
        # Find ranges to merge 
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            if intervals[index][1] >= newInterval[0]:
                if first_number > intervals[index][0]:
                    first_number = intervals[index][0]
                if second_number < intervals[index][1]:
                    second_number = intervals[index][1]
                intervals.pop(index)
            else:
                index += 1
        
        intervals.insert(index, [first_number, second_number])   
        return intervals    
