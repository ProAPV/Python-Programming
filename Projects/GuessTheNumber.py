import random

print(''' ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   _______   ________     
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|     ''')

computer_Guess = 0
attempts_left = 0
randomNumber = 0

computer_Guess = random.randint(0, 100)
print(computer_Guess)
difficulty_Level = str(input("""Do you want the difficulty level to be "hard" or "easy" ? """))

if difficulty_Level == "hard":
    attempts_left = 5
elif difficulty_Level == "easy":
    attempts_left = 10

while attempts_left > 0:
    user_Guess = int(input("Enter a number between 0-100: "))
    if user_Guess == computer_Guess:
        print("Congratulations!!! You guessed the correct number")
        attempts_left = -1
    elif user_Guess > computer_Guess:
        attempts_left-=1
        print(f"The number of attempts left are {attempts_left}")
        print("The number you guessed is higher than the number chose by the computer")
    elif user_Guess < computer_Guess:
        attempts_left-=1
        print(f"The number of attempts left are {attempts_left}")
        print("The number you guessed is lower than the number chose by the computer")

if attempts_left == 0:
    print("You were unable to guess the correct number")