class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        
        count = 1
        maxCount = 0

        for i in nums:
            if i - 1 not in n:
                for j in range(1, len(nums) + 1):
                    if i + j in n:
                        count = count + 1
                    else:
                        break
                maxCount = max(count, maxCount)
                count = 1

        return maxCount