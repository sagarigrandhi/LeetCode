class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        topk = sorted(nums_dict.items(), key = lambda x: x[1], reverse=True)[:k]
        topk_keys = []
        for i in range(len(topk)):
            topk_keys.append(topk[i][0])
        return topk_keys