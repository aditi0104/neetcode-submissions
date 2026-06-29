class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1
        total = 0
        while l < h:
            total = numbers[l] + numbers[h]
            if total == target:
                return [l + 1, h + 1]
            elif total > target:
                h = h - 1
            else:
                l = l + 1