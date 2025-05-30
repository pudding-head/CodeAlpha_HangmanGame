import random 

def hangman():
    words = ["python", "program", "algorithm", "variable", "function"]
    secret_word = random.choice(words).lower()
    guesses_left = 6
    correct_guesses = []  
    all_guesses = []      

    print("**********************************")
    print("Welcome to Hangman!!")
    print(f"Hint: The word is a programming term with {len(secret_word)} letters")

    while guesses_left > 0:

        display_word = ""
        for char in secret_word:
            if char in correct_guesses:
                display_word += char + " "
            else:
                display_word += "_ "
        print(display_word.strip())


        if all(char in correct_guesses for char in secret_word):
            print("\nCongratulations! You won!")
            print(f"The word was: {secret_word}")
            return


        while True:
            guess = input("\nGuess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter exactly one letter.")
            elif not guess.isalpha():
                print("Please enter a valid letter (a-z).")
            elif guess in all_guesses:
                print("You've already guessed that letter. Try another.")
            else:
                break

        all_guesses.append(guess)


        if guess in secret_word:
            correct_guesses.append(guess)
            print(f"Correct! '{guess}' is in the word.")
        else:
            guesses_left -= 1
            print(f"Incorrect! '{guess}' is not in the word. Guesses left: {guesses_left}")


    print("\nGame over! You've run out of guesses.")
    print(f"The word was: {secret_word}")

if __name__ == "__main__":
    hangman()