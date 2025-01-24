"""A package for parsing number strings in various formats."""

def parse_number(number_str: str) -> float:
    """Parse a string representation of a number into a float.

    Args:
        number_str (str): The string to parse

    Returns:
        float: The parsed number

    Examples:
        >>> parse_number('1,234.56')
        1234.56
        >>> parse_number('50%')
        0.5
        >>> parse_number('1.5k')
        1500.0
        >>> parse_number(' 2.3M ')
        2300000.0
    """
    if not isinstance(number_str, str):
        raise TypeError("Input must be a string")

    # Trim whitespace
    number_str = number_str.strip()

    # Handle empty string
    if not number_str:
        raise ValueError("Empty string is not a valid number")

    # Handle percentage
    if number_str.endswith('%'):
        return float(number_str.rstrip('%')) / 100

    # Remove commas
    number_str = number_str.replace(',', '')

    # Handle k/m/b suffixes
    multipliers = {
        'k': 1e3,
        'm': 1e6,
        'b': 1e9
    }

    # Check for magnitude suffixes
    if number_str[-1].lower() in multipliers:
        multiplier = multipliers[number_str[-1].lower()]
        number_str = number_str[:-1]
        return float(number_str) * multiplier

    return float(number_str)