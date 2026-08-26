class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num,0) + 1
        
        sortedlist = sorted(dictionary, key=dictionary.get, reverse=True)

        return sortedlist[:k]



       
        