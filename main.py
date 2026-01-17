from pwinput import pwinput

secret_word = ""
secret_letter_list = list(secret_word)
guess_letters = []
body_parts = 1
hanged_man = 7
playing = True

def play_again():
    continue_game = input("would you like to play again? Enter yes or no: ").lower()
    while True:
        if continue_game == "yes":
            return True
        if continue_game == "no":
            return False
        else:
            continue_game = input("Invalid input enter yes or no: ")

def check_word():
    word = pwinput("Player one enter a word: ", "*").lower()
    while True:
        if  word.isalpha() and len(word) >= 3:
            return word
        else:
            word = pwinput("Invalid input, please enter a word: ", "*")

def print_progress():
    for letter in secret_word:  # for each letter
        if letter in guess_letters:  # check if letter was guessed
            print(letter, end="")
        else:
            print("*", end="")
    print("")

def take_guess():
    chosen_letter = input("Player two guess a letter: ").lower()
    while True:
        if chosen_letter.isalpha() and len(chosen_letter) == 1:
            guess_letters.append(chosen_letter)
            return chosen_letter
        else:
            chosen_letter = input("Invalid input, please enter a letter: ")

def check_guess(guess, the_word):
    if guess in guess_letters and len(guess_letters) <= 0:
        print(f"You've guessed the letter: {guess} already.")
        return True
    elif guess in the_word:
        print(f"You've guessed the letter: {guess} and it's correct!")
        print_progress()
        return True
    else:
        print(f"You've guessed the letter: {guess} and it's incorrect!")
        print_progress()
        print(f"Only {(hanged_man - body_parts)} chance left.")
        return False

print("lets play Hangman!")
while playing:
    secret_word = check_word()
    #print(secret_word)
    #check_word(secret_word)

    while playing:
        if body_parts > hanged_man:
            print("     _______\n"
                  "    |       l\n"
                  "    |       l\n"
                  "  _____     l\n"
                  " | 0 0 |    l\n"
                  "  |###|     l\n"
                  "  --I--     l\n"
                  "I   I   I   l\n"
                  "I   I   I   l\n"
                  "M  ___  M   l\n"
                  "  I   I     l\n"
                  "  |   |     l\n"
                  "  I   I     l\n"
                  "            l\n"
                  "        ____l____\n")
            print(f"You lose!\n"
                  f"The word was '{secret_word}'.")
            if play_again():
                guess_letters.remove(guess_letters[0])
                break
            else:
                playing = False
        elif not check_guess(take_guess(), secret_word):
            body_parts += 1
            #print(body_parts)
        elif all(char in guess_letters for char in secret_word):
            print("You Win!!!")
            if play_again():
                guess_letters.remove(guess_letters[0])
                break
            else:
                playing = False
