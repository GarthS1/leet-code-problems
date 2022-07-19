# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters, combos, indexs = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}, [], [0] * len(digits)
        
        while indexs[0] < len(letters[digits[0]]):
            string =  ""
            for i in range(len(indexs)):
                string += letters[digits[i]][indexs[i]]
            combos.append(string)
            
            indexs[-1] += 1
            for i in range(len(indexs) -1, 0, -1):
                if indexs[i] == len(letters[digits[i]]):
                    indexs[i] = 0
                    indexs[i -1] += 1
            
        return combos
