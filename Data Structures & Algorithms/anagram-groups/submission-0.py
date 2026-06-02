class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sDict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sDict:
                sDict[sorted_s].append(s)
            else:
                sDict[sorted_s] = [s]
            
        newList = []
        
        for i in sDict:
            newList.append(sDict[i])
        
        return newList