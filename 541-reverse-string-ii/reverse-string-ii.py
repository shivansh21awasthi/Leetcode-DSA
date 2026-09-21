class Solution:

    def reverseStr(self, s: str, k: int) -> str:
        res = []
        buf = []
        is_k = True 
        for char in s:
            buf.append(char)
            if len(buf) == k:
                if is_k:
                    res.extend(buf[::-1]) 
                else:
                    res.extend(buf)

                buf = []  
                is_k = not is_k 
        if buf:
            if is_k:
                res.extend(buf[::-1])
            else:
                res.extend(buf)

        return "".join(res)