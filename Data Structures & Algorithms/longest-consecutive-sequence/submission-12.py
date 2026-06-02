class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = set(nums)

        count = 0
        maxCount = 0

        for i in n:
            if i - 1 not in n:
                count = 1
                while i + count in n:
                    count = count + 1
                if count > maxCount:
                    maxCount = count
                    count = 1

        return maxCount

