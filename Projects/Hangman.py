import random

#Step 1 

word_list = ["aardvaark", "baboon", "camel"] 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word1 = random.randint(0, len(word_list)-1)
chosen_word = word_list[chosen_word1]
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess1 = str(input("Enter the first letter"))
guess = guess1.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

present = chosen_word.find(guess)

#Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess

underscore = []
for x in range(len(chosen_word)):
    underscore+="_"

# for y in range(len(chosen_word)):
#     guess1 = str(input("Enter the first letter"))
#     guess = guess1.lower()
#     if chosen_word[y] == guess:
#             underscore[y] = guess
# print(underscore)

#TODO-2: - Loop through each position in the chosen

# y = 0
# maxTry = 6
# while "_" in underscore == True or maxTry != 0:
#     y+=1
#     guess1 = str(input("Enter the first letter"))
#     guess = guess1.lower()
#     if maxTry != 0:
#         if chosen_word[y] == guess:
#             underscore[y] = guess
#             maxTry+=0
#             if "_" in underscore == False:
#                 print("You Win")
#         elif chosen_word[y] != guess:
#             maxTry-=1
#             print(maxTry)
#             if maxTry == 0:
#                 print("You Loose")

x = 0
maxTry = 6
igc = 0
while x in range("_" in underscore == True or maxTry != 0):      #loop starts
    guess1 = str(input("Enter the first letter"))    #gtakes input    
    guess = guess1.lower()                           #makes input into lower case
    if maxTry != 0:                                  #makes condition as if max try is not 0
        if chosen_word[x] == guess:                  #makes another condition if all the letter are
            underscore[x] = guess
            print(underscore)
            igc == 1
        else:
            maxTry-=1

if maxTry != 0:
    print("You Loose Game Over")
else:
    print("Congrats, You win")