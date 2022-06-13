https://leetcode.com/problems/longest-substring-without-repeating-characters/
Runtime: 80 ms
Memory Usage: 14.3 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        longest_substring = ""
        current_substring = ""
        
        while index < len(s):
            if s[index] in current_substring:
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                current_substring = current_substring[1:]
            else:
                current_substring += s[index]
                index += 1
        
        if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
        
        return len(longest_substring)
            
