class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        total_pairs = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h = i + 1, len(nums) - 1
            while l<h:
                total = nums[i] + nums[l] + nums[h]
                if total > 0:
                    h = h - 1
                elif total < 0:
                    l = l + 1
                else:
                    total_pairs.append([nums[i], nums[l], nums[h]])
                    l = l + 1
                    while l<h and nums[l] == nums[l-1]:
                        l = l + 1
        return total_pairs
                
                