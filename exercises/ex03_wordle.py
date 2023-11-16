"""EX03 - Structured Wordle."""

__author__ = "730656260"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_word: str, search_character: str) -> bool:
    """Return True if search_word is found in search_character, else False."""
    assert len(search_character) == 1
    search_word_length = len(search_word)
    word_index: int = 0
    char_check: bool = False
    while not char_check and word_index < search_word_length:
        if search_character == search_word[word_index]:
            char_check = True
        else:
            word_index += 1
    return char_check


def emojified(wordle_secret: str, wordle_guess: str) -> str:
    """Return color-related emojis based on comparison of secret and guess attempt."""
    assert len(wordle_guess) == len(wordle_secret)
    wordle_guess_index: int = 0
    emoji: str = ""

    while wordle_guess_index < len(wordle_guess):
        character_check = contains_char(wordle_secret, wordle_guess[wordle_guess_index])
        if wordle_guess[wordle_guess_index] == wordle_secret[wordle_guess_index]:
            emoji += GREEN_BOX
        elif character_check:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        wordle_guess_index += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Determine if the length of the guessed word is correct."""
    wordle_guess: str = input(f"Enter a {expected_length} character word:")
    while len(wordle_guess) != expected_length:
        wordle_guess = input(f"That wasn't {expected_length} chars! Try again:")
    return wordle_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_counter: int = 1
    wordle_secret: str = "codes"
    win: bool = False
    while turn_counter <= 6 and not win:
        print(f"=== Turn {turn_counter}/6 ===")
        wordle_guess: str = input_guess(len(wordle_secret))
        print(emojified(wordle_secret, wordle_guess))
        if wordle_guess == wordle_secret:
            win = True
            print(f"You won in {turn_counter}/6 turns!")
        else:
            print("X/6 - Sorry, try again tomorrow!")

        turn_counter += 1


if __name__ == "__main__":
    main()