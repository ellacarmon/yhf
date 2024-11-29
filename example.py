from yhf.stock import StockAPI
from yhf.stock_history import StockHistoryAPI
from yhf.insights import InsightsAPI

if __name__ == "__main__":
    api_key = "your_api_key_here"

    # Initialize the APIs
    stock_api = StockAPI(api_key)
    history_api = StockHistoryAPI(api_key)
    insights_api = InsightsAPI(api_key)

    # Fetch stock data
    stock_data = stock_api.get_stock_data("AAPL")
    print("Stock Data:", stock_data)

    # Fetch stock history
    history_data = history_api.get_stock_history("AAPL")
    print("Stock History:", history_data)

    # Fetch insights
    insights = insights_api.get_insights("AAPL")
    print("Insights:", insights)
