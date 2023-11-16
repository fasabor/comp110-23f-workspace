"""Practice with Dictionary Functions."""

__author__ = "730656260"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Create a function that inverts the keys and values."""
    result: dict[str, str] = {}
    for key in x:
        result[x[key]] = key
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Function that returns the most frequent color in a dictionary."""
    result: dict[str, int] = {}
    for key in x:
        if x[key] in result:
            result[x[key]] += 1
        else:
            result[x[key]] = 1
    maxvalue = max(result.values())
    for key in result:
        if result[key] == maxvalue:
            return key
    return "No favorite color."


def count(x: list[str]) -> dict[str, int]:
    """Function that produces a dictionary with unique key values and corresponding values that are the number of times it appears in the list."""
    result: dict[str, int] = {}
    for key in x:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Function that produces a dictionary where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    result: dict[str, list[str]] = {}
    for key in x:
        if key[0] in result:
            result[key[0]].append(key)
        else:
            result[key[0]] = [key]
    return result


def update_attendance(x: dict[str, list[str]], weekday: str, student: str) -> dict[str, list[str]]:
    """A function that updates and adds a students name to the attendance list on a chosen day."""
    if weekday in x:
        x[weekday].append(student)
    else:
        x[weekday] = [student]
    return x
