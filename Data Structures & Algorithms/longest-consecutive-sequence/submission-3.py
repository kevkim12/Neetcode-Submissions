class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxCount = 1
        count = 1
        if nums == []:
            return 0

        for i in numSet:
            if i - 1 in numSet:
                continue
            else:
                if i + 1 in numSet:
                    num = i
                    for j in range(1, len(numSet) + 1):
                        if num + j in numSet:
                            count = count + 1
                            print(num + j)
                        else:
                            print("-")
                            break
                    if count > maxCount:
                        maxCount = count
                    count = 1
        
        return maxCount