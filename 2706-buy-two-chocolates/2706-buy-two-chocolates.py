class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        summed_prices = prices[0] + prices[1]
        return money - summed_prices if summed_prices <= money else money
        