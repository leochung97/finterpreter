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

    def save_report(report_type, ticker=None):
        if report_type == "market":
            report = market_research()
            filename = f"{FORMATTED_DATE}-markets-report.txt"
        elif report_type == "equity":
            filename = f"{FORMATTED_DATE}-{ticker}-report.txt"
        else:
            raise ValueError("Invalid report type")
    
        print(report)
        file_path = output_path / filename
        file_path.touch()
        file_path.write_text(report)

    if args.market:
        save_report("market")
    elif args.ticker:
        save_report("equity", args.ticker)
    else:
        print("Please provide a valid argument")