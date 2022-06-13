https://leetcode.com/problems/zigzag-conversion/
Runtime: 89 ms, faster than 48.96% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 13.9 MB, less than 74.92% of Python3 online submissions for Zigzag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        strings_array = []
        for i in range(numRows):
            strings_array.append("")
        
        current_row = 1
        incrementation = 1
        strings_array[0] += s[0]
        
        for i in range(1, len(s)):
            if current_row == numRows - 1 or current_row == 0:
                incrementation *= -1
            
            strings_array[current_row] += s[i]
            current_row += incrementation
        
        return "".join(strings_array)
        
