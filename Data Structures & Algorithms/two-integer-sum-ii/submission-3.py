class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[right] + numbers[left] == target:
                return [left + 1, right + 1]
            elif numbers[left] < target - numbers[right]:
                left = left + 1
            elif numbers[left] > target - numbers[right]:
                right = right - 1
                

            # [4, 6, 7, 8, 9]   t = 14