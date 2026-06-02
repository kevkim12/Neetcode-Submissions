class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:

            if "".join(sorted(s)) not in anagrams:
                anagrams["".join(sorted(s))] = [s]
            else:
                anagrams["".join(sorted(s))].append(s)

        l = []

        for v in anagrams.values():
            l.append(v)

        return l