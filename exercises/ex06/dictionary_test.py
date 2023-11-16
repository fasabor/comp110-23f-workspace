"""Creating test cases for functions created in EX06."""

__author__ = "730656260"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

def test_invert_two_keys() -> None:
    """Function that tests "invert" with numbers in str."""
    test: dict[str,str] = {"1": "2", "8": "9"}
    result = 