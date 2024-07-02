from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days between the given date and today's date.

    Args:
        date (str): The date string in the format 'YYYY-MM-DD'.

    Returns:
        int: The number of days between the given date and today's date. 
             Returns 0 if the date format is incorrect.

    Raises:
        ValueError: If the date format is incorrect.
    """
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        result = (converted_date - today).days
        return result
    except ValueError:
        print("Incorrect date format. Please use the format 'YYYY-MM-DD'")
        return 0

# Example usage:
days_difference = get_days_from_today("2021-10-09")
print(f"Number of days: {days_difference}")