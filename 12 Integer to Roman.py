https://leetcode.com/problems/integer-to-roman/
Runtime: 45 ms, faster than 95.91% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.9 MB, less than 79.11% of Python3 online submissions for Integer to Roman.
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_number = ""
        
        first_digit = num // 1000
        num = num % 1000
        second_digit = num // 100
        num = num % 100
        third_digit = num // 10
        num = num % 10
        fourth_digit = num 
        
        roman_number += 'M' * first_digit 
        
        if second_digit == 9:
            roman_number += 'CM'
        elif second_digit == 4:
            roman_number += 'CD'
        elif second_digit >= 5:
            roman_number += 'D'
            second_digit -= 5
            roman_number += 'C' * second_digit
        else:
             roman_number += 'C' * second_digit
        
        if third_digit == 9:
            roman_number += 'XC'
        elif third_digit == 4:
            roman_number += 'XL'
        elif third_digit >= 5:
            roman_number += 'L'
            third_digit -= 5
            roman_number += 'X' * third_digit
        else:
             roman_number += 'X' * third_digit
        
        if fourth_digit == 9:
            roman_number += 'IX'
        elif fourth_digit == 4:
            roman_number += 'IV'
        elif fourth_digit >= 5:
            roman_number += 'V'
            fourth_digit -= 5
            roman_number += 'I' * fourth_digit
        else:
             roman_number += 'I' * fourth_digit
            
        return roman_number
