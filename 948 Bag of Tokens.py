# https://leetcode.com/problems/bag-of-tokens/
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        left_index, right_index, score = 0, len(tokens) - 1, 0
        tokens.sort()
        
        while left_index <= right_index:
            if power >= tokens[left_index]:
                power -= tokens[left_index]
                score += 1
                left_index += 1
            elif tokens[right_index] > tokens[left_index] and score > 0:
                power += tokens[right_index] 
                score -= 1
                right_index -= 1
            else: 
                break
        
        return score
            
        
