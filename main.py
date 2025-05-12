from reports.query import query_perplexity
from reports.equity import equity_research
from reports.market import market_research
from reports.industry import industry_research
from trade.buy import prompt_user_buy
from trade.portfolio import show_portfolio
from trade.options import get_options_chain
from config import FORMATTED_DATE
from pathlib import Path
import argparse
import os
import shutil
from datetime import datetime

def move_old_files():
    outputs_dir = "outputs"
    old_dir = os.path.join(outputs_dir, "old")
    today = datetime.today().date()

    for filename in os.listdir(outputs_dir):
        file_path = os.path.join(outputs_dir, filename)

        if os.path.isdir(file_path) or filename == "old":
            continue

        try:
            date_str = filename.split("-")[0]
            file_date = datetime.strptime(date_str, "%Y.%m.%d").date()
        except (ValueError, IndexError):
            continue
            
        if file_date < today:
            dest_path = os.path.join(old_dir, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} to {old_dir}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Financial Research CLI Tool")
    parser.add_argument("-t", "--ticker", help="Research stock ticker to generate equity research report")
    parser.add_argument("-m", "--market", action="store_true", help="Research financial markets to generate market research report")
    parser.add_argument("-i", "--industry", help="Researches the latest developments in an industry to generate an industry research report")
    parser.add_argument("-b", "--buy", action="store_true", help="Opens buying trade confirmation options")
    parser.add_argument("-s", "--sell", action="store_true", help="Opens selling trade confirmation options")
    parser.add_argument("-p", "--portfolio", action="store_true", help="Displays current portfolio positions")
    parser.add_argument("-o", "--options", action="store_true", help="Opens options chain for a requested ticker")
    parser.add_argument("-q", "--query", action="store_true", help="Query Perplexity AI for information")
    args = parser.parse_args()

    output_path = Path("outputs")
    output_path.mkdir(parents=True, exist_ok=True)
    sections = ["Response", "Citations", "System Instructions", "User Instructions"]
    section_divider = "\n\n" + "=" * 92 + "\n\n"

    def save_report(report_type: str, ticker=None):
        if report_type == "market":
            report = market_research()
            filename = f"{FORMATTED_DATE}-markets-report.md"
        elif report_type == "equity":
            report = equity_research(args.ticker)
            filename = f"{FORMATTED_DATE}-{ticker}-report.md"
        elif report_type == "industry":
            report = industry_research(args.industry)
            filename = f"{FORMATTED_DATE}-{args.industry}-report.md"
        else:
            raise ValueError("Invalid report type")
    
        formatted_output = ""
        for section, content in zip(sections, report):
            formatted_output += f"## {section}\n\n{content}{section_divider}"
        file_path = output_path / filename
        file_path.touch()
        file_path.write_text(formatted_output)

    # Moves old reports to old folder automatically
    move_old_files()
    
    if args.market:
        save_report("market")
    elif args.ticker:
        save_report("equity", args.ticker)
    elif args.industry:
        save_report("industry")
    elif args.buy:
        prompt_user_buy()
    # elif args.sell:
    #     print("Sell trade confirmation")
    elif args.portfolio:
        show_portfolio()
    elif args.options:
        get_options_chain()
    elif args.query:
        query_perplexity()
    else:
        print("Please provide a valid argument")