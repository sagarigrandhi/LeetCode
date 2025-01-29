class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float("inf")
        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
        change = money - min1 - min2
        return change if change >= 0 else money
        