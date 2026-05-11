class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        left = [0] * len(nums)
        right = [0] * len(nums)

        for i in range(len(nums)):
            left[i] = prefix
            prefix *= nums[i]
        
        prefix = 1

        for i in range(len(nums)-1,-1,-1):
            right[i] = prefix
            prefix *= nums[i]
        
        return [left[i] * right[i] for i in range(len(nums))]


            
        