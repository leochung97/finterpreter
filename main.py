from reports.equity import equity_research
from reports.market import market_research
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Financial Research CLI Tool")
    parser.add_argument("-t", "--ticker", help="Research stock ticker to generate equity research report")
    parser.add_argument("-m", "--market", help="Research financial markets to generaate market research report")

    args = parser.parse_args()

    if args.market:
        report = market_research()
        print(report)
    elif args.ticker:
        report = equity_research(args.ticker)
        print(report)
    else:
        print("Please provide a valid argument")   