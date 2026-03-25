import logging
import os


def setup_logging():
    """
    Sets up logging to a file named 'trades.log' in the 'logs' directory.
    """

    # Ensure the 'logs' directory exists
    os.makedirs("logs", exist_ok=True)

    # Configure the logger and set the logging level to INFO
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a file handler that logs messages to 'trades.log' and set its logging level to INFO
    handler = logging.FileHandler("logs/trades.log")
    handler.setLevel(logging.INFO)

    # Create a logging formatter and set it for the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Set the formatter for the handler and add the handler to the logger
    handler.setFormatter(formatter)
    logger.addHandler(handler)
