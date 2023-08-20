import random

#Step 1 

word_list = ["aardvaark", "baboon", "camel"] 

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

choosen_word = word_list[random.randint(0, len(word_list)-1)]
print(choosen_word)

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess

underscore = []

for x in range(len(choosen_word)):
    underscore+="_"
print(underscore)

#Loop through each position in the chosen

maxtry = 6
over = 0

while maxtry > 0 and over == 0:
    guess = str(input("Enter your guess")).lower()
    underscor = 0
    for y in range(len(choosen_word)):
        if guess == choosen_word[y]:
            underscor = 1
            underscore[y]=guess
    print(underscore)
    if underscor==0:
        maxtry-=1
    elif "_" not in underscore:
        over = 1

if maxtry != 0:
    print("(❁´◡`❁)  (*/ω＼*)  ☆*: .｡. o(≧▽≦)o .｡.:*☆  ╰(*°▽°*)╯   You Win   Congrats")
else:
    print("X_X   You Loose    Game Over")