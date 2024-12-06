class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        res = {
            "[" : "]", "{":"}", "(":")"
        }
        for x in s:
            if x in res:
                stk.append(x)
            else:
                if not stk or res[stk.pop()] != x:
                    return False
        return not stk    
    

    