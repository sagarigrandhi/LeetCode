class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_i = []
        for i, num in enumerate(nums):
            nums_i.append((num, i))
        
        nums_i.sort()
        i, j = 0, len(nums_i) - 1 
        while i < j:
            curr_sum = nums_i[i][0] + nums_i[j][0]
            if curr_sum == target:
                return [min(nums_i[i][1], nums_i[j][1]), max(nums_i[i][1], nums_i[j][1])]
            elif curr_sum < target:
                i += 1
            else:
                j -= 1
        return [] 