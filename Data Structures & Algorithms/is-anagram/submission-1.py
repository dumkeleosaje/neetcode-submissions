class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}

        for i in s:
            set_s[i] = set_s.get(i,0) + 1
        
        for j in t:
            set_t[j] = set_t.get(j,0) + 1
        
        if set_s == set_t:
            return True

        return False