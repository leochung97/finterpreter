from reports.equity import equity_research
from reports.market import market_research
from reports.industry import industry_research
from config import FORMATTED_DATE
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Financial Research CLI Tool")
    parser.add_argument("-t", "--ticker", help="Research stock ticker to generate equity research report")
    parser.add_argument("-m", "--market", action="store_true", help="Research financial markets to generate market research report")
    parser.add_argument("-i", "--industry", help="Researches the latest developments in an industry to generate an industry research report")

    args = parser.parse_args()

    output_path = Path("outputs")
    output_path.mkdir(parents=True, exist_ok=True)
    sections = ["System Instructions","User Instructions", "Citations", "Response"]
    section_divider = "\n\n" + "=" * 100 + "\n\n"

    def save_report(report_type: str, ticker=None):
        if report_type == "market":
            report = market_research()
            filename = f"{FORMATTED_DATE}-markets-report.txt"
        elif report_type == "equity":
            report = equity_research(args.ticker)
            filename = f"{FORMATTED_DATE}-{ticker}-report.txt"
        elif report_type == "industry":
            report = industry_research(args.industry)
            filename = f"{FORMATTED_DATE}-{args.industry}-report.txt"
        else:
            raise ValueError("Invalid report type")
    
        formatted_output = ""
        for section, content in zip(sections, report):
            formatted_output += f"## {section}\n\n{content}{section_divider}"
        file_path = output_path / filename
        file_path.touch()
        file_path.write_text(formatted_output)

    if args.market:
        save_report("market")
    elif args.ticker:
        save_report("equity", args.ticker)
    elif args.industry:
        save_report("industry")
    else:
        print("Please provide a valid argument")