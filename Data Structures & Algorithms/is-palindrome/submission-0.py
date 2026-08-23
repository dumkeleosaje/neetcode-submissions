class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if list(filter(str.isalnum, s)) == list(filter(str.isalnum, reversed(s))):
            return True
        return False