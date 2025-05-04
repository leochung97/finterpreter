from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
from alpaca.trading.client import TradingClient
from alpaca.trading.stream import TradingStream
import alpaca_trade_api as tradeapi
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# OpenAI API
CLIENT = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)

# Alpaca Trade API

###### MIGHT HAVE TO MOVE ALPACA_API TO EACH TRADE FILE BECAUSE OF DIFFERENT API 
###### https://alpaca.markets/deprecated/docs/api-documentation/api-v2/

ALPACA_API = tradeapi.REST(
    key_id=os.getenv("ALPACA_KEY"),
    secret_key=os.getenv("ALPACA_SECRET"),
    base_url=os.getenv("ALPACA_ENDPOINT"),
    api_version="v2"
)

TRADING_CLIENT = TradingClient(os.getenv("ALPACA_KEY"), os.getenv("ALPACA_SECRET"))
TRADING_STREAM = TradingStream(os.getenv("ALPACA_KEY"), os.getenv("ALPACA_SECRET"), paper=True)

# Perplexity AI Available Models:
# sonar-deep-research
# sonar-reasoning-pro
# sonar-reasoning
# sonar-pro
# r1-1776 (offline chat model)
MODEL = "sonar-pro"

# Temperature controls the randomness of the response
# Values range from 0.0 and 2.0 with lower temperatures 
# being more deterministic and higher temperatures being more creative.
TEMPERATURE = 0.2

today = datetime.now()
FORMATTED_DATE = today.strftime("%Y.%m.%d")