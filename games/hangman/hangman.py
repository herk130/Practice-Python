from mimetypes import guess_all_extensions
import py_compile
from words import words
import random 

def get_word():
    word = random.choice(words)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 
    print("let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guessa letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
               print(guess, "is not in the word/")
               tries -= 1 
               guessed_letters.append(guess)
            else:
                print("good job,", guess, "is in the word!")       

        elif len(guess) == len(word) and guess.isalpha():

        else:
            print("not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")






def display_hangman(tries):
    stages = 
             