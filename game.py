import random
import datetime

# CONSTANTS
GREEN = 2
YELLOW = 1
BLACK = 0

#choose the word of the day
def get_today_word():
    file = open("answerbank.txt", "r")
    bank = file.read()
    av_words = list(map(str, bank.split()))
    dt = datetime.date
    random.seed(dt)
    today_word = random.choice(av_words)
    return today_word

#check to see if user's guess is valid
def valid_word(guess_word):
    #against bank of valid guesses
    is_valid = False
    with open("wordbank.txt", "r") as file:
        bank = file.read()
        if guess_word in bank:
            is_valid = True
    #against bank of potential answers
    with open("answerbank.txt", "r") as file:
        bank = file.read()
        if guess_word in bank:
            is_valid = True
    return is_valid

#compare the user's guess with the word of the day
def check_guess(guess, answer):
    arr_guess = list(guess)
    arr_answer = list(answer)
    arr_guess_code = [(letter, BLACK) for letter in arr_guess]

    #code the yellows
    i = 0
    while i < 5:
        if arr_guess[i] in arr_answer:
            arr_guess_code[i] = (arr_guess[i], YELLOW)
        i += 1
    #code the greens
    i = 0
    while i < 5:
        if arr_guess[i] == arr_answer[i]:
            arr_guess_code[i] = (arr_guess[i], GREEN)
        i += 1
    return arr_guess_code
