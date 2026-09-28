class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ''.join(c.lower() for c in s if c.isalnum())
        if alnum == alnum[::-1]:
            return True
        else:
            return False
        