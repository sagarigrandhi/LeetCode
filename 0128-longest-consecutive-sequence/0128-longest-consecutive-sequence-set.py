class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        visited = set(nums)
        
        for num in nums:
            prev_num = num - 1
            if prev_num not in visited:
                length = 1
                next_num = num + 1
                while next_num in visited:
                    length += 1
                    next_num += 1

                max_length = max(length, max_length)
        return max_length
    