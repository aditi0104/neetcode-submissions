class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVal = {}
        total = 0
        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevVal:
                return [prevVal[diff], index]
            prevVal[value] = index
            
