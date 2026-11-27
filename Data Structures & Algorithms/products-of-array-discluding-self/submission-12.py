class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        prefix = [1] * nums_length
        postfix = [1] * nums_length

        for index in range(nums_length):
            if index == 0:
                continue
            prefix[index] = nums[index-1]*prefix[index-1]

            postfix_index = -index-1
            postfix[postfix_index] = nums[postfix_index+1]*postfix[postfix_index+1]
            
        return [prefix[index]*postfix[index] for index in range(nums_length)]
