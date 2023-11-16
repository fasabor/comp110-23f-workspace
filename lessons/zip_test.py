"""Test my zip function."""

__author__ = "730656260"


from lessons.zip import zip


def test_two_empty_lists() -> None:
    """Test zip with empty lists."""
    list1: list[str] = []
    list2: list[int] = []
    assert zip(list1, list2) == {}


def test_same_length_lists() -> None:
    """Test zip with same length lists."""
    list1: list[str] = ["U", "N", "C"]
    list2: list[int] = [1, 2, 3]
    assert zip(list1, list2) == {"U": 1, "N": 2, "C": 3}


def test_diff_keys() -> None:
    """Test zip with different keys same values."""
    list1: list[str] = ["Balloons", "Plates", "Pears"]
    list2: list[int] = [1, 1, 1]
    assert zip(list1, list2) == {"Balloons": 1, "Plates": 1, "Cake": 1}