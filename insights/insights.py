from api.base import BaseAPIWrapper

class InsightsAPI(BaseAPIWrapper):
    def get_insights(self, symbol: str):
        """
        Fetch insights for a given stock symbol.
        """
        endpoint = f"v6/finance/insights"
        params = {"symbol": symbol}
        return self._make_request(endpoint, params)
