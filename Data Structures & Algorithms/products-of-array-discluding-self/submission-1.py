class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        left = [0] * len(nums)
        right = [0] * len(nums)
        # nums = [1,2,4,6]
        for i in range(len(nums)):
            # left = [0,0,0,0] - start
            # left = [1,0,0,0] - 1
            # left = [1,2,0,0] - 2
            # left = [1,2,8,0] - 3
            # left = [1,2,8,48] - 4
            left[i] = prefix
            # left = [1,0,0,0]
            # left = [1,1,0,0]
            # left = [1,1,2,0]
            # left = [1,1,2,8]
            prefix *= nums[i] # prefix = prefix * nums[i]
            # prefix = 1
            # prefix = 2
            # prefix = 8
            # prefix = 48
        
        prefix = 1
        # nums = [1,2,4,6]
        for i in range(len(nums)-1,-1,-1):
            # right = [0,0,0,0] - start
            # right = [0,0,0,6]
            # right = []
            right[i] = prefix # [0,0,0,1], 
            # right =[0,0,6,1]
            # right = [0,24,6,1]
            # right = [48,24,6,1]
            prefix *= nums[i]
            # prefix = 6
            # prefix = 24
            # prefix = 48
        
        return [left[i] * right[i] for i in range(len(nums))]


            
        