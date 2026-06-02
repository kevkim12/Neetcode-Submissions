import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        h = []

        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
            
        for key, v in d.items():
            heapq.heappush(h, (v, key))

        l = heapq.nlargest(k, h)

        freq = []
        for i, v in l:
            freq.append(v)

        return freq