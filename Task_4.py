from datetime import datetime, timedelta

def parse_birthday(birthday_str) -> datetime.date:
    """
    Parse a birthday string into a date object.

    Args:
        birthday_str (str): The birthday string in 'YYYY.MM.DD' format.

    Returns:
        datetime.date: The parsed birthday date.

    Raises:
        ValueError: If the birthday string is not in the correct format.
    """

    try:
        return datetime.strptime(birthday_str, "%Y.%m.%d").date()
    except ValueError:
        raise ValueError("Invalid birthday format. Use 'YYYY.MM.DD'.")

def calculate_next_weekday(date: datetime.date) -> datetime.date:
    """
    Calculate the next weekday if the given date falls on a weekend.

    Args:
        date (datetime.date): The date to check.

    Returns:
        datetime.date: The next weekday date if the given date is a weekend, otherwise the same date.
    """

    if date.weekday() >= 5:
        return date + timedelta(days=(7 - date.weekday()))
    return date

def get_upcoming_birthdays(users: list) -> list:
    """
    Get a list of users with their upcoming birthday congratulations dates.

    Args:
        users (list): A list of dictionaries with user information, each containing 'name' and 'birthday' keys.

    Returns:
        list: A list of dictionaries with user information and their congratulations dates.
    """

    try:
        today = datetime.today().date()
        end_date = today + timedelta(days=7)

        result = []

        for user in users:
            name = user["name"]
            user_birthday = parse_birthday(user["birthday"])

            # Set the birthday to the current year
            birthday_this_year = user_birthday.replace(year=today.year)

            # If the birthday has already occurred this year, set it to next year
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Check if the birthday is within the next 7 days
            if today <= birthday_this_year <= end_date:
                congratulation_date = birthday_this_year

                # Adjust the congratulation date to the next weekday if it falls on a weekend
                congratulation_date = calculate_next_weekday(congratulation_date)
            else:
                congratulation_date = birthday_this_year

            # Add the user and their congratulation date to the result list
            result.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

        return result

    except ValueError as e:
        print(f"Error: {e}")
        return []

# Example usage:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of birthday people:", upcoming_birthdays)