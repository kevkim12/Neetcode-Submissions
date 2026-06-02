class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        lst = []

        for s in strs:
            srt = "".join(sorted(s))
            if srt not in d:
                d[srt] = [s]
            else:
                d[srt].append(s)

        for v in d.values():
            lst.append(v)
        
        return lst