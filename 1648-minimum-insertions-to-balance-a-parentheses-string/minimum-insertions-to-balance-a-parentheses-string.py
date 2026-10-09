class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open += 1
                i += 1
            else:  
                if i+1 < n and s[i+1] == ')':
                    if open > 0:
                        open -= 1
                    else:
                        insertions += 1
                    i += 2
                else:
                    if open > 0:
                        open -= 1
                        insertions += 1 
                    else:
                        insertions += 2 
                    i += 1

        insertions += open * 2
        return insertions
