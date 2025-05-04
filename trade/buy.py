from config import ALPACA_API

def buy_order(symbol: str, qty: int, price: float = None):
    order_type = 'limit' if price else 'market'
    
    try:
        order = ALPACA_API.submit_order(
            symbol = symbol.upper(),
            qty = qty,
            side = 'buy',
            type = order_type,
            time_in_force = 'gtc',
            limit_price = price
        )
        # print(f"Order submitted: {order.side} {order.qty} {order.symbol} at {order.limit_price or 'Market Price'}")
        print(f"Order: {order}")
        return order
    
    except Exception as e:
        print(f"Error placing order: {e}")
        return None
    
def prompt_user_buy():
    try:
        symbol = input("Enter a ticker: ").strip().upper()
        qty = int(input("Enter number of shares to buy: "))
        price = input("Enter a price or press enter for market order: ")
        price = float(price) if price else None
        buy_order(symbol, qty, price)
    
    except ValueError as e:
        print(f"Invalid input format: {e}")