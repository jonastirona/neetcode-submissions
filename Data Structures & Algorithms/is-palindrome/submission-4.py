class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        while len(s) > 1:
            if s[0] not in alphabet:
                s = s[1:]
                continue
            if s[-1] not in alphabet:
                s = s[:len(s)-1]
                continue
            if s[0] != s[-1]:
                return False
            
            s = s[1:len(s)-1]

        return True