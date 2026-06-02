class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        ans = 0

        for num in seq:
            if num - 1 not in seq:
                curr = num
                cnt = 0
                while curr in seq:
                    curr += 1
                    cnt += 1
                ans = max(cnt, ans)
        return ans