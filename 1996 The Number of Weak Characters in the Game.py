#https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        num_characters, max_char, old_max_char = 0, [0,0], [0,0]       
        properties.sort(key=lambda x: x[0])
        
        for index in range(len(properties) - 1, -1, -1):
            if max_char[1] < properties[index][1]:
                if max_char[0] != properties[index][0]:
                    old_max_char = max_char
                max_char = properties[index]
                
            if (properties[index][1] < max_char[1] and properties[index][0] < max_char[0]) or (properties[index][1] < old_max_char[1] and properties[index][0] < old_max_char[0]):
                num_characters += 1
                
        return num_characters
