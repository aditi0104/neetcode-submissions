class Solution:
    def findMin(self, nums: List[int]) -> int:
        # result = nums[0]
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     if nums[l] < nums[r]:
        #         result = min(result, nums[l])
        #         break
        #     mid = (l + r)//2
        #     result = min(result, nums[mid])
        #     if nums[l] <= nums[mid]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return result
        l, h = 0, len(nums) - 1
        res = nums[0]

        while l <= h:
            if nums[l] < nums[h]:
                res = min(res, nums[l])
                break
            mid = (l + h)//2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        return res





























