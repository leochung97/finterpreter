from config import TRADING_CLIENT, TRADING_STREAM

def show_portfolio():
    account = TRADING_CLIENT.get_account()
    # print(account)
    positions = TRADING_CLIENT.get_all_positions()
    # print(positions)
    
    for position in positions:
        ticker = position.symbol
        quantity = position.qty
        avg_entry_price = f"${position.avg_entry_price}"
        current_price = f"${position.current_price}"
        change_today = "{:.2f}".format(float(position.change_today))
        percentage_change = "{:.2f}".format((float(position.current_price) - float(position.avg_entry_price)) / float(position.avg_entry_price) * 100)
        print(f"Ticker: {ticker}, Quantity: {quantity}, Avg Entry Price: {avg_entry_price}, Current Price: {current_price}, Change Today: {change_today}%, Percentage Change: {percentage_change}%")

# async def update_stream(data):
#     print(data)

# TRADING_STREAM.subscribe_trade_updates(update_stream)
# TRADING_STREAM.run()