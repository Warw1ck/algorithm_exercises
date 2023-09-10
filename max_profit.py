prices = [7, 1, 5, 3, 6, 4]


def max_profit(prices):
    profit = 0
    min_prise = prices[0]
    for i in range(len(prices)-1):
        min_prise = min(min_prise, prices[i])
        profit = max(prices[i] - min_prise, profit)
    return profit


