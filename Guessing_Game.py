secret_word = "Legion"
guess =""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        if guess != secret_word:
            print("Strike")
            print(guess_count)
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You suck!")
else:
    print("You win!")
