class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sDict = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in sDict:
                sDict[s].append(i)
            else:
                sDict[s] = [i]
        
        sList = []
        for v in sDict.values():
            sList.append(v)

        return sList