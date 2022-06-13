https://leetcode.com/problems/longest-palindromic-substring/
Runtime: 151 ms, faster than 97.95% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.8 MB, less than 90.68% of Python3 online submissions for Longest Palindromic Substring.
  
  class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
            
        longest_palindrome = s[0]
        length_longest_palindrome = 1       
        middle_index = 0
        
        while length_longest_palindrome < len(s) - 1:
            left_index = middle_index - 1
            right_index = middle_index + 1
            
            while right_index < len(s) and s[middle_index] == s[right_index]:
                right_index += 1
                middle_index += 1
            
            while left_index > -1 and right_index < len(s) and s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            #print(s[left_index + 1:right_index])
            
            if length_longest_palindrome < right_index - left_index - 1:
                longest_palindrome = s[left_index + 1:right_index ]
                length_longest_palindrome = len(longest_palindrome)

            middle_index += 1 
            
        return longest_palindrome
    
