class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letters1 = {}
        letters2 = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in letters1:
                letters1[letter] = 1
            else:
                letters1[letter] += 1

        for letter in t:
            if letter not in letters2:
                letters2[letter] = 1
            else:
                letters2[letter] += 1

        for key,value in letters1.items():
            if key not in letters2:
                return False
            elif letters2[key] != value:
                return False

        return True