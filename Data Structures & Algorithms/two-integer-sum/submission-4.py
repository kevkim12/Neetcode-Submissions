class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for n in range(len(nums)):
            if target - nums[n] in d:
                return [d[target - nums[n]], n]
            else:
                d[nums[n]] = n