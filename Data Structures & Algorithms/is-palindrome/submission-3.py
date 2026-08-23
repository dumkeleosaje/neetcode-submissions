class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        s = s.strip()
        for char in s:
            if char.isalnum():
                newStr = newStr + char.lower()
        
        if newStr == "".join(reversed(newStr)):
            return True
        return False