from binance import enums
from .client import BinanceClient
import logging

logger = logging.getLogger(__name__)


class Order:
    """
    Represents a trade order with methods to execute different types of orders.
    """

    def __init__(self, symbol, quantity, client: BinanceClient, price=None):
        """
        Initialize the Order object with symbol, quantity, client, and optional price.

        :param self: Self instance of the Order class
        :param symbol: Symbol to trade (e.g., "BTCUSDT")
        :param quantity: Quantity to trade
        :param client: BinanceClient instance to execute the order
        :param price: Price for LIMIT orders (optional)
        """
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.client = client

    def buy_limit(self, client):
        """
        Create a buy limit order using the Binance client.

        :param self: Self instance of the Order class
        :param client: BinanceClient instance to execute the order
        :return: Response from the Binance API after creating the order
        """
        order_params = {
            "symbol": self.symbol,
            "side": enums.SIDE_BUY,
            "type": enums.ORDER_TYPE_LIMIT,
            "quantity": self.quantity,
            "price": self.price,
            "timeInForce": enums.TIME_IN_FORCE_IOC,
        }
        return client.create_future_order(order_params)

    def sell_limit(self, client):
        """
        Create a sell limit order using the Binance client.

        :param self: Self instance of the Order class
        :param client: BinanceClient instance to execute the order
        :return: Response from the Binance API after creating the order
        """
        order_params = {
            "symbol": self.symbol,
            "side": enums.SIDE_SELL,
            "type": enums.ORDER_TYPE_LIMIT,
            "quantity": self.quantity,
            "price": self.price,
            "timeInForce": enums.TIME_IN_FORCE_GTC,
        }
        return client.create_future_order(order_params)

    def buy_market(self, client):
        """
        Create a buy market order using the Binance client.

        :param self: Self instance of the Order class
        :param client: BinanceClient instance to execute the order
        :return: Response from the Binance API after creating the order
        """
        order_params = {
            "symbol": self.symbol,
            "side": enums.SIDE_BUY,
            "type": enums.ORDER_TYPE_MARKET,
            "quantity": self.quantity,
        }
        return client.create_future_order(order_params)

    def sell_market(self, client):
        """
        Create a sell market order using the Binance client.

        :param self: Self instance of the Order class
        :param client: BinanceClient instance to execute the order
        :return: Response from the Binance API after creating the order
        """
        order_params = {
            "symbol": self.symbol,
            "side": enums.SIDE_SELL,
            "type": enums.ORDER_TYPE_MARKET,
            "quantity": self.quantity,
        }
        return client.create_future_order(order_params)
