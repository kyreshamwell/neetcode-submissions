class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i, num in enumerate(nums):
            seen = target - num
            if seen in prevMap:
                return [prevMap[seen], i]
            prevMap[num] = i
        