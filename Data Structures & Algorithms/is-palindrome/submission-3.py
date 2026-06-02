class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = ""

        for i in s:
            if i.isalnum():
                newS = newS + i.lower()

        return newS == newS[::-1]