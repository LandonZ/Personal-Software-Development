#Hangman in python

from wordslist import words #can import the variable
import random

#dictionary of key:() ASCII ART
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

#displaying hangman function
def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

#list of characters
def display_hint(hint):
    print(" ".join(hint)) #joins each letter in hint with space

#function for answer
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words) #get a random word for hangman
    hint = ["_"] * len(answer) #get number of underscore elements for answer length.
    # can use * operator
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses) #display man based off wrong guesses
        display_hint(hint)
        guess = input("Enter a letter: ").lower() #make all guesses lower

        if len(guess) != 1 or not guess.isalpha(): #must be a letter and alphabetical chararcter
            print("Invalid input")
            continue #skips this loop

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer: #if letter in the answer string
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint: #if no underscores left in hint
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses == len(hangman_art) - 1: #since length is 7 and starts at 1
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

#call main when running this file directly
if __name__ == '__main__':
    main()