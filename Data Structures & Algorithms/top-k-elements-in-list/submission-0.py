import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        heap = []

        for i in nums:
            if i in freq:
                freq[i] = freq[i] + 1
            else:
                freq[i] = 1

        for key, v in freq.items():
            heapq.heappush(heap, (v, key))

        largest = heapq.nlargest(k, heap)
        output = []
        for freq, num in largest:
            output.append(num)

        return output