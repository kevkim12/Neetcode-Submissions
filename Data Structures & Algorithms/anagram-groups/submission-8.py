class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grp = {}
        ans = []

        for s in strs:
            key = ''.join(sorted(s))

            if key in grp:
                grp[key].append(s)
            else:
                grp[key] = [s]
        
        return list(grp.values())