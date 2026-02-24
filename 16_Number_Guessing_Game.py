# Number Guessing Game

import random
best_score=None

while True:
    secret_number=random.randint(1,100)
    attempts_left=7
    attempts_used=0

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have chosen a number between 1 and 100.")
    print("You have 7 attempts!")

    while attempts_left>0:
        try:
            guess=int(input("\n Enter your guess: "))
            attempts_used+=1
            attempts_left-=1

            if guess==secret_number:
                print(f" Congratulations ! You guessed it in { attempts_used} attempts")

                if best_score is None or attempts_used<best_score:
                    best_score=attempts_used
                    print("New Best Score!")

                print(f"Best Score:{best_score} attempt(s)")
                break

            elif guess>secret_number:
                print("Too high!")

            else:
                print("Too low!")

            if abs(guess-secret_number)<=5:
                print("Hint : You are VERY close")

        except ValueError:
            print("Please enter a valid number")

    if attempts_left ==0 and guess!=secret_number:
        print(f"\n Game over ! The number wa {secret_number}")
    
    play_again=input("\n Dou you want to play again? (yes/no): ").lower()

    if play_again!='yes':
        print("Thanks for playing....")
        break