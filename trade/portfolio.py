from config import ALPACA_API

def show_portfolio():
    positions = ALPACA_API.list_positions()
    print(positions)
    
    for position in positions:
        print(f"Ticker: {position.symbol}, Quantity: {position.qty}, Avg. Entry Price: {position.avg_entry_price}, Cost Basis: {position.cost_basis}, Current Price: {position.current_price}, Today's Change: {position.change_today}")
