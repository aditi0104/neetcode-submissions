class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            #select the left array assuming we are there and then based 
            #on conditions deciding whether to search on the right or left 
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #select the right array assuming we are there and then based 
            #on conditions deciding whether to search on the right or left 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1






































            
            
        