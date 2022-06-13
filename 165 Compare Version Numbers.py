https://leetcode.com/problems/compare-version-numbers/
Runtime: 40 ms, faster than 60.98% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.9 MB, less than 75.85% of Python3 online submissions for Compare Version Numbers.
  class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        index_1, index_2 = 0, 0
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        version1 = list(map(int, version1))
        version2 = list(map(int, version2))
       
        if len(version1) < len(version2):
            for x in range(len(version2) - len(version1)):
                version1.append(0)
        elif len(version1) > len(version2):
            for x in range(len(version1) - len(version2)):
                version2.append(0)
            
        for x, y in zip(version1, version2):
            if x < y:
                return -1
            elif x > y:
                return 1
            
        return 0
