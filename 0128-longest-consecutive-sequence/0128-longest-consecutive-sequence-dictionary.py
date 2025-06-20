class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        visited_dict = {}
        for num in nums:
            visited_dict[num] = False
        
        count = 0
        max_count = 0
        for num in nums:
            count = 1
            prev_num = num - 1
            while prev_num in visited_dict and visited_dict[prev_num] == False:
                count += 1
                visited_dict[prev_num] = True
                prev_num -= 1
            
            next_num = num + 1
            while next_num in visited_dict and visited_dict[next_num] == False:
                count += 1
                visited_dict[next_num] = True
                next_num += 1
            
            max_count = max(count, max_count)
        return max_count
