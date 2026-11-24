class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for index, number in enumerate(nums):
            if (first_index:=nums_dict.get(target-number)) is not None:
                return [first_index,index]
            if number not in nums_dict:
                nums_dict[number] = index
