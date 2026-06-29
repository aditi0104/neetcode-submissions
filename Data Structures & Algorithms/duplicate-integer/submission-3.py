class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset = set()
        # for num in nums:
        #     if num in hashset:
        #         return True
        #     hashset.add(num)
        # return False

        #this solution scans all the elements always and has no early stopping 
        #hence not good for interviews
        return len(set(nums)) < len(nums)        
        