def buy_and_sell_stock(stock_prices: list):
    buy, sell = 0, 1
    max_profit: int = 0
    while(sell < len(stock_prices)):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit
            else:
                buy = sell
            sell += 1

    return max_profit
