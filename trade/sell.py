from config import ALPACA_API

def sell_order(symbol: str, qty: int, price: float = None):
    order_type = 'limit' if price else 'market'