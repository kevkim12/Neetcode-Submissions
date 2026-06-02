import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elements = []
        freq = {}
        ans = []

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for num, occ in freq.items():
            heapq.heappush(elements, (occ, num))

        for occ, num in heapq.nlargest(k, elements):
            ans.append(num)

        return ans
