secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): # świetne takie warunkowanie
    if guess_count < guess_limit:  #  if 0++<3
        guess = input("Enter a secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True  # bez wciecia nie działało

if out_of_guesses:  #  =if TRUE
    print("Out of Guesses, YOU LOSE!")
else:
    print("You found it")
