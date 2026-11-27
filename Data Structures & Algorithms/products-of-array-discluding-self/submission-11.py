class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        prefix = [1] * nums_length
        postfix = [1] * nums_length

        for index in range(nums_length):
            if index == 0:
                continue
            prefix[index] = nums[index-1]*prefix[index-1]

        for index in range(-2, -nums_length-1, -1):
            postfix[index] = nums[index+1]*postfix[index+1]
            
        return [prefix[index]*postfix[index] for index in range(len(nums))]
