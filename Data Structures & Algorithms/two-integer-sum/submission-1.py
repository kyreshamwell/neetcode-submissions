class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        hashmap = {}

        for i, num in enumerate(nums):
            seen = target - num
            if seen  in hashmap:
                return [hashmap[seen], i]
            hashmap[num] = i
            
        