#https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_index = 0
        index = len(citations) - 1 
        
        while index != -1 and h_index < citations[index]:
            h_index += 1
            index -= 1 
        
        return h_index
