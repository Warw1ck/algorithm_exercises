prices = [7, 1, 5, 3, 6, 4]


def max_profit(prices):
    day = 0
    profit = 0
    for i in range(len(prices)):
        day_price = prices[i]
        if i == len(prices)-1:
            break
        max_price_profit = max(prices[i+1: len(prices)])
        day_profit = max_price_profit - day_price
        if day_profit > profit:
            day = i
            profit = day_profit

    print(profit)



max_profit(prices)