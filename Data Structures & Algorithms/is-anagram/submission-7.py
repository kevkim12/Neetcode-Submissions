class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        for letter in t:
            if letter not in letters:
                return False
            else:
                letters[letter] -= 1

        for value in letters.values():
            if value != 0:
                return False

        return True