class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}

        for word in strs:
            sorts = ''.join(sorted(word))
            hashmap[sorts] = hashmap.get(sorts, [])
            hashmap[sorts].append(word)
        
        return list(hashmap.values())



        