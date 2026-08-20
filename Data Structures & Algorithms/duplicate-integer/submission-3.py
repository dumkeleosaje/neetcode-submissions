class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        
        for ele in nums:
            key = ele
            dictionary[key] = dictionary.get(key,0) + 1

        for j in dictionary:
            if dictionary[j] >= 2:
                return True
           
        return False
        