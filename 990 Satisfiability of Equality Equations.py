#https://leetcode.com/problems/satisfiability-of-equality-equations/
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals = []
        
        for equation in equations:
            if equation[1] == '=':
                equals.append({equation[0], equation[3]})
        
        #print(equals)
        
        changed = True
        while changed:
            changed = False
            i, j = 0, 0 
            while i < len(equals):
                j = i + 1
                while j < len(equals):
                    if not equals[i].isdisjoint(equals[j]):
                        equals[i] = equals[i].union(equals[j])
                        equals.pop(j)
                        changed = True
                    j += 1
                i += 1
        
        #print(equals)
        
        for equation in equations:
            if equation[1] == '!':
                if equation[0] == equation[3]:
                    return False
                for word in equals:
                    if equation[0] in word and equation[3] in word:
                        return False
        
        return True 
