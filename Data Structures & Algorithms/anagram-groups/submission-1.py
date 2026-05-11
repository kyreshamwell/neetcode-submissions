class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # key : [values]
        # sorted : [actual]

        hashmap = {}

        for words in strs:
            sort = tuple(sorted(words))
            hashmap[sort] = hashmap.get(sort, [])
            hashmap[sort].append(words)
        return list(hashmap.values())

        