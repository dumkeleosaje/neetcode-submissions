class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        s = s.strip()
        for char in s:
            if char.isalnum():
                newStr = newStr + char.lower()
        
        if newStr == newStr[::-1]:
            return True
        return False