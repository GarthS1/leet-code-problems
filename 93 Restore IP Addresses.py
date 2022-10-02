# https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        array = []
        def recursive(s, append, digit, array):
            if digit == 4 and s[0] == '0' and len(s) != 1:
                return
            elif digit == 4 and s[0] == '0' and len(s) == 1: 
                array.append(str(append + s))
            elif digit == 4 and int(s) <= 255: 
                array.append(str(append + s))
            else:
                if s[1:] and int(s[0]) <= 255:
                    recursive(s[1:], str(append + s[0] + '.'), digit + 1, array) 
                if s[2:] and int(s[:2]) <= 255 and s[0] != '0':
                    recursive(s[2:], str(append + s[:2] + '.'), digit + 1, array) 
                if s[3:] and int(s[:3]) <= 255 and s[0] != '0':
                    recursive(s[3:], str(append + s[:3] + '.'), digit + 1, array)
            
        recursive(s, "", 1, array)
        return array 
            
        
