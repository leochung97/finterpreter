from config import ALPACA_API, TRADING_CLIENT, TRADING_STREAM, OPTION_CLIENT

import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Options Imports
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical.stock import StockHistoricalDataClient, StockLatestTradeRequest

from alpaca.data.live.option import OptionDataStream
from alpaca.data.requests import (
    OptionBarsRequest,
    OptionTradesRequest,
    OptionLatestQuoteRequest,
    OptionLatestTradeRequest,
    OptionSnapshotRequest,
    OptionChainRequest
)
from alpaca.trading.requests import (
    GetOptionContractsRequest,
    GetAssetsRequest,
    MarketOrderRequest,
    GetOrdersRequest,
    ClosePositionRequest
)
from alpaca.trading.enums import (
    AssetStatus,
    ExerciseStyle,
    OrderSide,
    OrderType,
    TimeInForce,
    QueryOrderStatus,
    ContractType
)
from alpaca.common.exceptions import APIError

def get_options_chain():
    try:
        symbol = input("Enter a ticker: ").strip().upper()
        request_params = OptionChainRequest(
            underlying_symbol = symbol,
        )
        response = OPTION_CLIENT.get_option_chain(request_params)
        print(response)
    except APIError as e:
        print(f"Error fetching options chain: {e}")
    return