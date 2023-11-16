"""Ex02 - A One Shot Wordle."""

__author__ = "730656260"

wordle_word: str = ("python")
secret_length: int = len(wordle_word)
wordle_guess: str = input(f"What is your {secret_length}-letter guess:")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

wordle_index: int = 0
emoji_guess: str = ""

while len(wordle_guess) != len(wordle_word):
    wordle_guess = input(f"That was not {secret_length} letters! Try again:")

if len(wordle_guess) == len(wordle_word):
    while wordle_index < len(wordle_word):
        if wordle_guess[wordle_index] == wordle_word[wordle_index]:
            emoji_guess += GREEN_BOX
        else:
            wordle_variable: bool = False
            wordle_alternate: int = 0

            while not wordle_variable and wordle_alternate < len(wordle_word):
                if wordle_word[wordle_alternate] == wordle_guess[wordle_index]:
                    wordle_variable = True 
                else: 
                    wordle_alternate += 1
            if wordle_variable: 
                emoji_guess += YELLOW_BOX
            else:
                emoji_guess += WHITE_BOX
        wordle_index += 1

print(emoji_guess)
if wordle_guess == wordle_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
