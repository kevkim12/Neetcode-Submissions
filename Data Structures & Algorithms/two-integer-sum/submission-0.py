class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nDict = {}
        for i, n in enumerate(nums):
            if target - n in nDict:
                if i < nDict[target-n]:
                    return [i, nDict[target-n]]
                else:
                    return [nDict[target-n], i]
            else:
                nDict[n] = i