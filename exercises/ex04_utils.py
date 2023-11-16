"""EX03 - 'list' Utility Functions."""
__author__ = 730656260


def all(list: list[int], value: int) -> bool:
    """Check list elements to see if equal to specified value."""
    if len(list) == 0:
        return False
    list_index: int = 0 
    while list_index < len(list):
        if list[list_index] != value:
            return False
        list_index += 1
    return True


def max(input: list[int]) -> int:
    """Return maximum list value or return error if list empty."""
    if len(input) == 0: 
        raise ValueError("max() argument is empty list")
    list_index: int = 1
    maximum_value: int = input[0]
    while list_index < len(input):
        if input[list_index] > maximum_value:
            maximum_value = input[list_index]
        else:
            list_index += 1
        list_index += 1
    return maximum_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determine if every element at every index in two lists is equal."""
    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) != len(list2):
        return False
    list_index: int = 0
    while list_index < len(list1) and list_index < len(list2):
        if list1[list_index] != list2[list_index]:
            return False
        list_index += 1
    return True