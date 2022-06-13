https://leetcode.com/problems/shifting-letters/
Runtime: 823 ms, faster than 96.76% of Python3 online submissions for Shifting Letters.
Memory Usage: 27.2 MB, less than 79.92% of Python3 online submissions for Shifting Letters.
 
  class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sum_shift = sum(shifts)
        shift_string = ''
        char_list = []

        for x in range(len(s)):
            char_list.append(chr( ((ord(s[x]) -97 + sum_shift) % 26) + 97))
            sum_shift -= shifts[x]
            
        return "".join(char_list)
