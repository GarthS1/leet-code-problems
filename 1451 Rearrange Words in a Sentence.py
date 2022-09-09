# https://leetcode.com/problems/rearrange-words-in-a-sentence/
class Solution:
    def arrangeWords(self, text: str) -> str:
        heap = []
        index_start = 0
        index_end = 0
        #Need to keep original order by having words of the same length slightly higher 
        increment_counter = 1 / (pow(10,5) + 1) 
        counter = 0
        
        while index_end < len(text):
            if text[index_end] == ' ':
                heappush(heap, (index_end - index_start + counter, text[index_start:index_end]))
                index_start = index_end + 1
                counter += increment_counter
            index_end += 1
        
        heappush(heap, (index_end - index_start + counter, text[index_start:index_end]))
        
        ordered = ""
        while heap:
            ordered += heappop(heap)[1] + ' '
        
        return ordered[:-1].capitalize()
        
        
