class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
            
        for k in t:
            if k in t_dict:
                t_dict[k] += 1
            else:
                t_dict[k] = 1
        

        if s_dict == t_dict:
            return True
        else:
            return False

        