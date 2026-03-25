# Validation functions for user input


def validate_quantity(value: str) -> float:
    """
    Validate that the quantity is a positive number.

    :param value: The quantity as a string.
    :type value: str
    :return: The validated quantity as a float.
    :rtype: float
    """
    try:
        quantity = float(value)
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        return quantity
    except ValueError:
        raise ValueError("Invalid quantity")


def validate_price(value: str) -> float:
    """
    Validate that the price is a positive number.

    :param value: The price as a string.
    :type value: str
    :return: The validated price as a float.
    :rtype: float
    """
    try:
        price = float(value)
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        return price
    except ValueError:
        raise ValueError("Invalid price")
