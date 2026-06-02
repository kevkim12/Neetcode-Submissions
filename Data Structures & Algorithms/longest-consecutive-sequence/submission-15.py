class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxCount = 0
        count = 1
        n = set(nums)

        for i in n:
            if i - 1 not in n:
                while i + count in n:
                    print(i + count)
                    count += 1
                maxCount = max(count, maxCount)
                count = 1

        return maxCount