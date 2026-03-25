import questionary
import logging

from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.orders import Order
from bot.logging_config import setup_logging
import utils


# Setup logging and load environment variables
setup_logging()
load_dotenv()

logger = logging.getLogger("bot.orders")


def main():
    print("Futures Trading Bot")

    try:
        client = BinanceClient()
    except Exception as e:
        print(f"Error: {e}")
        return

    # Step 1: Select symbol
    symbol = utils.select_symbol(client)
    if not symbol:
        return

    # Step 2: Select order type
    order_type = utils.select_order_type()
    if not order_type:
        return

    # Step 3: Select side
    side = utils.select_side()
    if not side:
        return

    # Step 4: Quantity
    quantity = utils.get_quantity()
    if not quantity:
        return

    # Step 5: Price (if LIMIT)
    price = utils.get_price_if_needed(order_type)
    if order_type == "LIMIT" and price is None:
        return

    # Step 6: Confirm details
    utils.confirm_trade(
        {
            "symbol": symbol,
            "price": price,
            "type": order_type,
            "side": side,
            "quantity": quantity,
        }
    )

    if not questionary.confirm("Do you want to place this order?").ask():
        print("Order cancelled.")
        return

    # Step 7: Execute
    order = Order(
        client=client,
        symbol=symbol,
        quantity=quantity,
        price=price,
    )

    try:
        response = utils.execute_order(order, order_type, side)

        logger.info(
            f"Placed {side} {order_type} order for {quantity} {symbol} at price {price if price else 'MARKET'}"
        )

        utils.print_order(response)

    except Exception as e:
        logger.error(
            f"Order for {quantity} {symbol} at price {price if price else 'MARKET'} failed"
        )
        print(f"Error placing order: {e}")


if __name__ == "__main__":
    main()
