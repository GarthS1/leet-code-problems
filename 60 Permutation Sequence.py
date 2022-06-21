'''
Runtime: 40 ms, faster than 76.04% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.9 MB, less than 78.48% of Python3 online submissions for Permutation Sequence.
'''

import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        final = ""
        
        while n > 0:
            # Region the number falls into 
            current_range = math.factorial(n - 1)
            index = (k -1) // current_range 
            
            # Remove number as we can no longer use it
            final += str(nums[index])
            del nums[index]
            
            n -= 1
            # Mod to find the next range 
            k = k % current_range
        
        return final
        
