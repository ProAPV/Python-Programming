import random
word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
for letter in chosen_word:
   display += "_"
  
print(f"Guess this word: {display}")
maxTry = 6

gameWon = 0
lenChoosenWord = len(chosen_word)
underScore = '_'

while (maxTry > 0 and gameWon == 0):
  guess = ((str)(input("Guess a letter"))).lower()
  
  isGuessCorrect = 0
  for x in range(lenChoosenWord):
    if guess == chosen_word[x]:
      display[x] = guess
      isGuessCorrect = 1
  print(display)
  if (isGuessCorrect == 0):
      maxTry -= 1
      print(f"Max try remaining {maxTry}")
  elif underScore not in display:
      gameWon = 1
  
if (gameWon == 1):
  print("@@@@@@@You won the game@@@@@@@")
  print(display)
elif (maxTry == 0):
  print("Hang till death Game over")
