import random

def parse_input(min_str: str, max_str: str, quantity_str: str) -> tuple:
    """
    Parse and convert input strings to integers.

    Args:
        min_str (str): Minimum value string.
        max_str (str): Maximum value string.
        quantity_str (str): Quantity string.

    Returns:
        tuple: A tuple containing parsed integers (min_num, max_num, quantity).
    """
    min_num = int(min_str)
    max_num = int(max_str)
    quantity = int(quantity_str)
    return min_num, max_num, quantity

def validate_input(min_num: int, max_num: int, quantity: int) -> bool:
    """
    Validate the input values.

    Args:
        min_num (int): Minimum value.
        max_num (int): Maximum value.
        quantity (int): Quantity of numbers.

    Returns:
        bool: True if input values are valid, False otherwise.
    """

    # Validate the range of min and max values
    if min_num >= max_num:
        print("'min' must be less than 'max'.")
        return False
    
    # Validate the quantity of numbers to generate
    if quantity <= 0:
        print("Quantity must be a positive integer.")
        return False
    return True

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generate a sorted list of unique random numbers within a specified range.

    Args:
        min_value (int): The minimum value of the range (inclusive).
        max_value (int): The maximum value of the range (inclusive).
        quantity (int): The number of unique random numbers to generate.

    Returns:
        list: A sorted list of unique random numbers within the specified range.

    Raises:
        ValueError: If any of the arguments 'min_value', 'max_value', or 'quantity' are not integers.
    """
    try:
        min_num, max_num, quantity = parse_input(min, max, quantity)
    except ValueError:
        print("Invalid input. Arguments 'min', 'max', and 'quantity' must be integers.")
        return []
    
    if not validate_input(min_num, max_num, quantity):
        return []


    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min_num, max_num))
        
    sorted_list = sorted(unique_numbers)

    return sorted_list

# Example usage:
lottery_numbers = get_numbers_ticket(1, 49, 3)
print(f"Your lottery numbers: {lottery_numbers}")