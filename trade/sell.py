from config import ALPACA_API

def sell_order(symbol: str, qty: int, price: float = None, order_type: str = 'market'): 
    try:
        order_data = {
            'symbol': symbol.upper(),
            'qty': qty,
            'side': 'sell',
            'type': order_type,
            'time_in_force': 'gtc'
        }
    except Exception as e:
        print(f"Error placing order: {e}")
        return None
