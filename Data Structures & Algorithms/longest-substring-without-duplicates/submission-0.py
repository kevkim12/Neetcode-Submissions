class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        chars = set()
        longest = 0

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                longest = max(longest, len(chars))  # Update longest here
            else:
                chars.remove(s[l])
                l += 1

        return longest