class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, i in enumerate(nums):
            if i in nums[index+1:]:
                return True
        return False