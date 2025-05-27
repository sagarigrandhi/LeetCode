class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        
        for k in t:
            s_dict[k] -= 1

        return all([count == 0 for count in s_dict.values()])

