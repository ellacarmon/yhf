from .base import BaseAPIWrapper
from typing import Dict, List, Optional, Union
from datetime import datetime

class StockAPI(BaseAPIWrapper):
        """
        A wrapper for the YH Finance API that provides methods to access stock market data.
        """

        def __init__(self, api_key: str):
            """
            Initialize the Yahoo Finance API wrapper.

            Args:
                api_key (str): API key for authentication
            """
            super().__init__(api_key)

        def get_stock_quote(self, symbol: str) -> Dict:
            """
            Get stock quote data for a specific symbol.

            Args:
                symbol (str): Stock symbol (e.g., 'AAPL')

            Returns:
                Dict: Stock quote data including price, volume, and metadata
            """
            endpoint = f"v6/finance/quote/"
            params = {"symbol": symbol}
            return self._make_request(endpoint, params)

        def get_stock_data(self, symbol: str, range: str = "1mo", interval: str = "1d", include_comparisons: bool = True) -> Dict:
            """
            Get stock data for a specific symbol.

            Args:
                symbol (str): Stock symbol (e.g., 'AAPL')
                range (str): Time range for data (e.g., '1d', '5d', '1mo', '1y')
                interval (str): Data interval (e.g., '1d', '1wk', '1mo')
                include_comparisons (bool): Whether to include comparison data

            Returns:
                Dict: Stock data including price, volume, and metadata
            """
            endpoint = f"v8/finance/chart/{symbol}"
            params = {
                "range": range,
                "interval": interval,
                "includeComparisons": str(include_comparisons).lower()
            }
            return self._make_request(endpoint, params)

        def get_stock_meta(self, symbol: str) -> Dict:
            """
            Get metadata for a specific stock.

            Args:
                symbol (str): Stock symbol

            Returns:
                Dict: Stock metadata including exchange info, trading periods, etc.
            """
            response = self.get_stock_data(symbol, range="1d")
            if response and "chart" in response:
                return response["chart"]["result"][0]["meta"]
            return {}

        def get_stock_price(self, symbol: str) -> float:
            """
            Get current market price for a stock.

            Args:
                symbol (str): Stock symbol

            Returns:
                float: Current market price
            """
            meta = self.get_stock_meta(symbol)
            return meta.get("regularMarketPrice", 0.0)

        def get_price_history(self, symbol: str,range: str = "1mo") -> Dict[str, List[float]]:
            """
            Get historical price data for a stock.

            Args:
                symbol (str): Stock symbol
                range (str): Time range for historical data

            Returns:
                Dict: Historical price data including open, high, low, close prices
            """
            response = self.get_stock_data(symbol, range=range)
            if not response or "chart" not in response:
                return {}

            indicators = response["chart"]["result"][0]["indicators"]["quote"][0]
            return {
                "open": indicators["open"],
                "high": indicators["high"],
                "low": indicators["low"],
                "close": indicators["close"],
                "volume": indicators["volume"]
            }

        def get_comparison_data(self, symbol: str, range: str = "1mo") -> Dict[str, Dict]:
            """
            Get comparison data for a stock (e.g., against other stocks or indices).

            Args:
                symbol (str): Stock symbol
                range (str): Time range for comparison data

            Returns:
                Dict: Comparison data for different symbols
            """
            response = self.get_stock_data(symbol, range=range, include_comparisons=True)
            if not response or "chart" not in response:
                return {}

            comparisons = {}
            for comp in response["chart"]["result"][0].get("comparisons", []):
                comparisons[comp["symbol"]] = {
                    "high": comp["high"],
                    "low": comp["low"],
                    "open": comp["open"],
                    "close": comp["close"]
                }
            return comparisons

        def get_dividend_events(self,symbol: str, range: str = "1mo") -> List[Dict]:
            """
            Get dividend events for a stock.

            Args:
                symbol (str): Stock symbol
                range (str): Time range for dividend data

            Returns:
                List[Dict]: List of dividend events with amount and date
            """
            response = self.get_stock_data(symbol, range=range)
            if not response or "chart" not in response:
                return []

            events = response["chart"]["result"][0].get("events", {})
            dividends = events.get("dividends", {})

            return [
                {
                    "date": datetime.fromtimestamp(timestamp),
                    "amount": data["amount"]
                }
                for timestamp, data in dividends.items()
            ]

        def get_trading_periods(self, symbol: str) -> Dict:
            """
            Get trading periods for a stock.

            Args:
                symbol (str): Stock symbol

            Returns:
                Dict: Trading period information including pre-market, regular, and post-market
            """
            meta = self.get_stock_meta(symbol)
            return meta.get("currentTradingPeriod", {})

        def get_market_range(self, symbol: str) -> Dict[str, float]:
            """
            Get 52-week range for a stock.

            Args:
                symbol (str): Stock symbol

            Returns:
                Dict: 52-week high and low prices
            """
            meta = self.get_stock_meta(symbol)
            return {
                "52_week_high": meta.get("fiftyTwoWeekHigh", 0.0),
                "52_week_low": meta.get("fiftyTwoWeekLow", 0.0)
            }

        def get_earnings_data(self, symbol: str) -> Dict[str, Union[float, str]]:
            """
            Get earnings data for a stock.

            Args:
                symbol (str): Stock symbol

            Returns:
                Dict: Earnings data including EPS, revenue, and earnings date
            """
            meta = self.get_stock_quote(symbol)
            return {
                "earnings_start": meta.get("earningsTimestampStart", 0.0),
                "earnings_end": meta.get("earningsTimestampEnd", 0.0),
                "earnings_date": datetime.fromtimestamp(float(meta.get("earningsTimestamp", 0.0)))
            }