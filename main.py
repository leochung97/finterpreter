from reports.equity import equity_research
from reports.market import market_research
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Financial Research CLI Tool")
    parser.add_argument("-t", "--ticker", help="Research stock ticker to generate equity research report")
    parser.add_argument("-m", "--market", action="store_true", help="Research financial markets to generate market research report")

    args = parser.parse_args()

    if args.market:
        print(market_research())
    elif args.ticker:
        print(equity_research(args.ticker))
    else:
        print("Please provide a valid argument")