from binance.client import Client
import os


class BinanceClient:
    """
    Wrapper around the Binance API client to handle authentication and common operations.
    """

    def __init__(self, use_testnet: bool = True):
        """
        Initialize the Binance client with API key and secret from environment variables.

        :param self: Self instance of the BinanceClient class
        :param use_testnet: Whether to use the testnet.
        :type use_testnet: bool
        """
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        if not api_key or not api_secret:
            raise ValueError("API key and secret must be set in environment variables.")
        try:
            self.client = Client(api_key, api_secret, testnet=use_testnet)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Binance API")

    def create_future_order(self, kwargs):
        """
        Create a futures order using the Binance client.

        :param self: Self instance of the BinanceClient class
        :param kwargs: Order parameters to pass to the Binance API
        :return: Response from the Binance API after creating the order
        """
        return self.client.futures_create_order(**kwargs)

    def get_price(self, symbol: str):
        """
        Get the current price of a symbol using the Binance client.

        :param self: Self instance of the BinanceClient class
        :param symbol: Symbol to get the price for (e.g., "BTCUSDT")
        :type symbol: str
        :return: Current price information for the symbol
        """
        return self.client.get_symbol_ticker(symbol=symbol)

    def get_symbols(self):
        """
        Returns a list of top 10 trading pairs that are currently active on Binance Futures.

        :param self: Self instance of the BinanceClient class
        """
        exchange_info = self.client.get_exchange_info()
        return [
            s["symbol"]
            for s in exchange_info["symbols"]
            if s["status"] == "TRADING" and s["symbol"].endswith("USDT")
        ][:10]
