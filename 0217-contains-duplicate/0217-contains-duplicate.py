class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        for i in range(len(nums) - 1):
            if nums_sorted[i] == nums_sorted[i+1]:
                return True
        return False


        