import requests

class BaseAPIWrapper:
    BASE_URL = "https://yfapi.net/"  # Base API URL

    def __init__(self, api_key: str):
        """
        Initialize the base wrapper with the API key.
        """
        self.api_key = api_key
        self.headers = {
            "x-api-key": self.api_key
        }

    def _make_request(self, endpoint: str, params: dict = None):
        """
        Internal method to make GET requests to the API.
        """
        url = self.BASE_URL + endpoint
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
