# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      # Use math to cacualte answer.
      # Example grid of 3 by 7, to reach the bottom we need to arrange the following moves DDRRRRRR. 
      # We thus can use combination logic to caculate all possible combonations 
      return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)
