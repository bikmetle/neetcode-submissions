class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for index, num in enumerate(nums):
            if index == 0:
                continue
            prefix[index] = nums[index-1]*prefix[index-1]

        index = 0
        for num in reversed(nums):
            index -= 1
            if index == -1:
                continue
            postfix[index] = nums[index+1]*postfix[index+1]
            
        return [prefix[index]*postfix[index] for index in range(len(nums))]

