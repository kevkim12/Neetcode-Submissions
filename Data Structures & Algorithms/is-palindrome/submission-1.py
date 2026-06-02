class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""

        for i in s:
            if i.isalnum() == True:
                newS = newS + i.lower()

        left = 0
        right = len(newS) - 1
        while left < right:
            if newS[left] == newS[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True
