import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        heap = []

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for num, freq in d.items():
            heapq.heappush(heap, (freq, num))

        print(heap)

        largestHeap = heapq.nlargest(k, heap)
        print(largestHeap)

        for freq, num in largestHeap:
            ans.append(num)
        
        return ans