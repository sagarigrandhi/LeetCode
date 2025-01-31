class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        valid = [0] * 26
        for i in range(len(s)):
            valid[ord(s[i]) -  ord('a')] += 1
            valid[ord(t[i]) - ord('a')] -= 1
        return all([count == 0 for count in valid])
        