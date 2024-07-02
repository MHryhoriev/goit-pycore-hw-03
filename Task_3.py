import re

def remove_non_digit_chars(phone_number: str) -> str:
    """
    Remove all characters from the phone number string except digits and '+'.

    Args:
        phone_number (str): The input phone number string.

    Returns:
        str: The phone number string with only digits and '+' remaining.
    """
    
    pattern = r"[^\d+]"
    return re.sub(pattern, "", phone_number)

def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to standard format, keeping only digits and the leading '+'.
    If the phone number doesn't start with an international code, add '+38'.

    Args:
        phone_number (str): The input phone number string.

    Returns:
        str: The normalized phone number string.
    """

    normalized_phone_number = remove_non_digit_chars(phone_number)

    if not normalized_phone_number.startswith("+"):
        if normalized_phone_number.startswith("380"):
            normalized_phone_number = f"+{normalized_phone_number}"
        else:
            normalized_phone_number = f"+38{normalized_phone_number}"

    return normalized_phone_number

# Example usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)