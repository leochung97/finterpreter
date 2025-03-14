This is a financial report builder using Perplexity AI's Sonar LLM.

The purpose of this algorithm is to build a first-glimpse report of an inputted stock ticker.
The algorithm will send a request to Sonar to gather as much information on the ticker using publicly available sources in the manner of an equity researcher.
The generated report will be structured similar to a real equity research report, complete with valuation tools. 

To run this program, you will need python3 and a Perplexity AI API key.
Steps:
1. `git clone` the repository.
2. In the directory, create a `.env` file and add `API_KEY={YOUR_PERPLEXITY_AI_API_KEY}`.
3. In your terminal, run `python main.py`; When prompted for a ticker, enter your ticker.