class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        n = len(s)
        for c in s:
            if c == '1':
                count += 1
        s_new = ''
        s_new = '1' * (count - 1) + '0' * (n - count) + '1' 
        return s_new