class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        chars = set()

        for right in range(len(s)):
            if s[right] not in chars:
                chars.add(s[right])
                longest = max(longest, right - left + 1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])

                longest = max(longest, right - left + 1)
        
        return longest