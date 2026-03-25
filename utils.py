import questionary
from bot.orders import Order
from bot.validators import validate_quantity, validate_price


# Color codes for terminal output
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"


# Input functions for CLI steps


def select_symbol(client):
    """
    Select a trading pair from the available symbols and display its current price.

    :param client: BinanceClient instance to fetch symbols and prices
    :return: Selected symbol or None if user exits
    """
    symbols = client.get_symbols()
    symbols.append("EXIT")

    symbol = questionary.select("Select a trading pair:", choices=symbols).ask()

    if symbol == "EXIT":
        return None

    price = client.get_price(symbol).get("price")
    print(f"{symbol} is trading at ${price}")

    return symbol


def select_order_type():
    """
    Select the order type (LIMIT or MARKET) for the trade.

    """
    order_type = questionary.select(
        "Select order type:", choices=["LIMIT", "MARKET", "EXIT"]
    ).ask()

    return None if order_type == "EXIT" else order_type


def select_side():
    """
    Select the order side (BUY or SELL) for the trade.
    """
    side = questionary.select(
        "Select order side:", choices=["BUY", "SELL", "EXIT"]
    ).ask()

    return None if side == "EXIT" else side


def get_quantity():
    """
    Prompt the user to enter the quantity for the trade and validate it.
    """
    quantity = questionary.text("Enter quantity:").ask()

    try:
        return validate_quantity(quantity)
    except ValueError as e:
        print(str(e))
        return None


def get_price_if_needed(order_type):
    """
    If the order type is LIMIT, prompt the user to enter the price and validate it.

    :param order_type: The type of order (LIMIT or MARKET)
    :return: Validated price or None if not needed or invalid
    """
    if order_type != "LIMIT":
        return None

    price = questionary.text("Enter price:").ask()

    try:
        return validate_price(price)
    except ValueError:
        print("Invalid price.")
        return None


# Function to execute the order based on the selected order type and side


def execute_order(order: Order, order_type: str, side: str):
    """
    Execute the order based on the specified order type and side.

    :param order: An instance of the Order class containing the order details and client information.
    :type order: Order
    :param order_type: The type of order to execute, either "LIMIT" or "MARKET".
    :type order_type: str
    :param side: The side of the order, either "BUY" or "SELL".
    :type side: str
    """
    if order_type == "LIMIT":
        return (
            order.buy_limit(client=order.client)
            if side == "BUY"
            else order.sell_limit(client=order.client)
        )
    else:
        return (
            order.buy_market(client=order.client)
            if side == "BUY"
            else order.sell_market(client=order.client)
        )


# Function to print order details in a formatted way


def print_order(response):
    """
    Print the details of the executed order in a formatted manner.

    :param response: The response from the Binance API after executing the order, containing details like symbol, order ID, status, quantity, and order type.
    """
    symbol = response["symbol"]
    order_id = response["orderId"]
    status = response["status"]
    quantity = response["origQty"]
    order_type = response["type"]

    print()
    print(f"{GREEN}{symbol} {order_type} ORDER SUCCESS!{RESET}")
    print(f"{WHITE}ID:{RESET} {order_id}")
    print(f"{WHITE}STATUS:{RESET} {GREEN}{status}{RESET}")
    print(f"{WHITE}QUANTITY:{RESET} {quantity}")
    print()


def confirm_trade(order):
    """
    Display the trade details for confirmation before placing the order.

    :param order: A dictionary containing the trade details such as symbol, price, order type, side, and quantity.
    """
    symbol = order["symbol"]
    price = order["price"]
    order_type = order["type"]
    side = order["side"]
    quantity = order["quantity"]

    print()
    print(f"{GREEN}CONFIRM TRADE{RESET}")
    print(f"{WHITE}PAIR:{RESET} {symbol}")
    print(f"{WHITE}PRICE:{RESET} ${price}")
    print(f"{WHITE}TYPE:{RESET} {order_type}")
    print(f"{WHITE}SIDE:{RESET} {side}")
    print(f"{WHITE}QUANTITY:{RESET} {quantity}")
    print()
