"""Combining two lists into a dictionary."""

__author__ = "730656260"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Function that combines two seperate lists into a dictionary."""
    if len(list1) != len(list2):
        print("Lists are not of equal length")
        return {}
    dictionary: dict[str, int] = {}
    i: int = 0
    while i < len(list1):
        dictionary[list1[i]] = list2[i]
        i += 1
    return dictionary
    

test1: list[str] = ["Happy", "Tuesday"]
test2: list[int] = [1, 2]

print(zip(test1, test2))
