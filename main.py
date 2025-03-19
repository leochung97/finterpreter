from reports.equity import equity_research
from reports.market import market_research
from config import FORMATTED_DATE
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Financial Research CLI Tool")
    parser.add_argument("-t", "--ticker", help="Research stock ticker to generate equity research report")
    parser.add_argument("-m", "--market", action="store_true", help="Research financial markets to generate market research report")

    args = parser.parse_args()

    output_path = Path("outputs")
    output_path.mkdir(parents=True, exist_ok=True)

    if args.market:
        market_report = market_research()
        print(market_report)
        file_path = output_path / f"{FORMATTED_DATE}-markets-report.txt"
        file_path.touch()
        file_path.write_text(market_report)
    elif args.ticker:
        equity_report = equity_research(args.ticker)
        print(equity_report)
        file_path = output_path / f"{FORMATTED_DATE}-{args.ticker}-report.txt"
        file_path.touch()
        file_path.write_text(equity_report)
    else:
        print("Please provide a valid argument")