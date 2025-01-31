class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return [i, nums_dict[nums[i]]]
            else:
                second = target - nums[i]
                nums_dict[second] = i
        