class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()

        left, right = 0, len(newStr)-1

        while left < right:
            leftchar, rightchar = newStr[left], newStr[right]
            if leftchar != rightchar:
                return False

            else:
                left += 1
                right -=1
               
        return True