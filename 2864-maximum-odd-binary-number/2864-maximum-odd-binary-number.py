class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_count = [0] * 2
        s_list = list(s)
        for val in s_list:
            if val == '0':
                s_count[0] += 1
            else:
                s_count[1] += 1
        s_new = ''
        s_new += '1' * (s_count[1] - 1)
        s_new += '0' * (s_count[0])
        s_new += '1'
        return s_new
        