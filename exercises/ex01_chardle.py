"""Ex01 - Chardle - A cute step toward Wordle."""
__author__ = "730656260"

chardle_word: str = input("Enter a 5-character word:")
if len(chardle_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

chardle_character: str = input("Enter a single character:")
if len(chardle_character) != 1:
    print(" Error: Character must be a single character.")
    exit()

print("Searching for " + chardle_character + " in " + chardle_word)

chardle_index: int = 0
total_chardle_instances: int = 0 

if chardle_word[0] == chardle_character:
    print(chardle_character + " found at index " + str(chardle_index))
    total_chardle_instances = (total_chardle_instances + 1) 
if chardle_word[1] == chardle_character:
    chardle_index = 1
    total_chardle_instances = (total_chardle_instances + 1) 
    print(chardle_character + " found at index " + str(chardle_index))
if chardle_word[2] == chardle_character:
    chardle_index = 2
    total_chardle_instances = (total_chardle_instances + 1)
    print(chardle_character + " found at index " + str(chardle_index))
if chardle_word[3] == chardle_character:
    chardle_index = 3
    total_chardle_instances = (total_chardle_instances + 1)
    print(chardle_character + " found at index " + str(chardle_index))
if chardle_word[4] == chardle_character:
    chardle_index = 4
    total_chardle_instances = (total_chardle_instances + 1)
    print(chardle_character + " found at index " + str(chardle_index))

if total_chardle_instances == 0:
    print("No instances of " + chardle_character + " found in " + chardle_word)
if total_chardle_instances == 1:
    print(str(total_chardle_instances) + " instance of " + chardle_character + " found in " + chardle_word)
if total_chardle_instances > 1:
    print(str(total_chardle_instances) + " instances of " + chardle_character + " found in " + chardle_word)