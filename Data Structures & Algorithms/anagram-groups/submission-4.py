class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        ans = []
        
        for s in strs:
            new_s = ''.join(sorted(s))
            if not new_s in words:
                words[new_s] = [s]
            else:
                words[new_s].append(s)

        for v in words.values():
            ans.append(v)

        return ans