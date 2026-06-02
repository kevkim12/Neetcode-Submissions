class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)

        maxCount = 0
        for i in n:
            if i - 1 not in n:
                count = 0
                while (i + count) in n:
                    count = count + 1
                maxCount = max(count, maxCount)

        return maxCount