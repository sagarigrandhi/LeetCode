class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            nums_dict[num] = i
