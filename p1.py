import random
def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    guess_history = []
    for i in range(7):
        guess = int(input("Guess the number between 1 and 100: "))
        attempts = attempts + 1
        attempts_left = 7 - attempts
        guess_history.append(guess)
        if guess < number:
            print("Too low! enter a higher number")
            print(f"you have {attempts_left} attempts left ")
        elif guess > number:
            print("Too high! enter a lower number")
            print(f"you have {attempts_left} attempts left ")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print("Your guesses were: ", guess_history)
            break
    else:
        print("you failed.You used all 7 attempts")
        print("The correct number was: ", number)
        print("your guesses were:", guess_history)
name = input('what is your name? ')
print(f'Welcome "{name}" to our guess game')
while True:
 asking = input('Do you wanna play the game "yes/no"? ')
 if asking == "yes":
   print("Sound good.Lets start")
   guess_game()
   break
 elif asking == "no":
    print("oppss,your first guess is already wrong.Now,you have to play the game")
    guess_game()
    break
 else:
    print("wrong command.choose yes or no")

while True:
  again = input('Do you want play the game again?"yes/no"? ')
  if again == "yes":
    print('I see!you\'ve enjoyed the game')
    guess_game()
  elif again == "no":
    print("Hopefully you've enjoyed the game.Come to play again another time")
    break
  else:
    print("So, you are messing with us!Not bad,try again next time")
    break