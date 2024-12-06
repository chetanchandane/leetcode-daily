def isPalindrome(s):
        s = s.lower()
        print(s)
        nams = {" ","!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/", "~", "`"}
        i, j = 0, len(s)-1
        while i < j:
            # print(f'Checking {s[i]} and {s[j]}')
            if s[i] in nams:
                i += 1
            elif s[j] in nams:
                j -= 1
            else:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True   



print(isPalindrome("A man, a plan, a canal: Panama"))