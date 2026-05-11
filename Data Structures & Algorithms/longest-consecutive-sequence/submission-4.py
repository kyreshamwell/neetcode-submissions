class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new = sorted(nums)
        prev = new[0]
        count = 1
        best = 1
        for num in new:
            if num == prev:
                pass
            elif num - prev == 1:
                count += 1
                best = max(best, count)
            else:
                count = 1
            prev = num
        return best
        