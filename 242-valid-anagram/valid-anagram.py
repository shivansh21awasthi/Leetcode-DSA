class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=len(t)
        s2=len(s)
        hs=sorted(list(s))
        hs1=sorted(list(t))

        if s1!=s2:
            return False
        else:
            if hs==hs1:
                return True
            else:
                return False    
                

        