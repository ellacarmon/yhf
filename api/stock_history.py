from .base import BaseAPIWrapper

class StockHistoryAPI(BaseAPIWrapper):
    def get_stock_history(self, symbol: str, interval: str = "1d", range_: str = "1mo"):
        """
        Fetch historical stock data.
        """
        endpoint = "v8/finance/chart"
        params = {"symbol": symbol, "interval": interval, "range": range_}
        return self._make_request(endpoint, params)
