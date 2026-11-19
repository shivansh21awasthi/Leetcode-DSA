     

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        p = 0
        q = len(cleaned) - 1
        while p < q:
            if cleaned[p] != cleaned[q]:
                return False
            p += 1
            q -= 1
        return True        

        