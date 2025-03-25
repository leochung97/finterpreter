from config import ALPACA_API

def place_order(symbol: str, qty: int, price: float = None):
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
        print(f"Order submitted: {order.side} {order.qty} {order.symbol} @ {order.limit_price}")
        return order
    
    except:
        print(f"Error placing order: {e}")
        return None
    
