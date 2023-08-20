############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

# import random
# user = 0
# computer = 0

# def deal_card(cards):
#     card = random.choice(cards)
#     return card

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# one = int((deal_card(cards))) # Change name of all 4 variables
# two = int((deal_card(cards)))
# cone = int((deal_card(cards)))
# ctwo = int((deal_card(cards)))

# computer = cone + ctwo # Change the name of variable

# def smallerThan17(cards, computer):
#     if computer < 17:
#         computer+=int((deal_card(cards)))
#         return computer

# def computerfinal(computer):
#     if smallerThan17(cards, computer) == True:
#         print(f"The sum of the computers cards is {computer}")
#     elif computer > 21:
#         print("You Win")
#     return computer

# def sum(cards, one, two, user):
#     user = one + two
#     if one != 11 and two != 11:
#         print(f"The sum of your cards is {user}")
#         q = str(input('Would you like to take another card ? Type "y" for if you want to take it and "n" if you do not want to take it: '))
#         if q == "y": # Change name of user
#             one = user
#             two = int((deal_card(cards)))
#             sum(cards, one, two, user)
#         if q == "n":
#             computerfinal(cone, ctwo, computer)
#             print(user)
#     elif one == 11 or two == 11:
#         if user > 21:
#             print("Bust")
#             return
#         elif user == 21:
#             print("BlackJack!!! You Win !!!!!!!")
#             return
#         elif user < 21:
#             print(f"The sum of your cards is {user}")
#             q = str(input('Would you like to take another card ? Type "y" for if you want to take it and "n" if you do not want to take it: '))
#             if q == "y":
#                 one = user
#                 two = int((deal_card(cards)))
#                 sum(cards, one, two, user)
#             elif q == "n":
#                 computerfinal(cone, ctwo, computer)
#                 print(user)
#     return user

# if sum(cards, one, two, user, ) > computerfinal(cone, ctwo, computer):
#     print("Congratulation!!!!! You Win !!!!!!!!!!!!!")
# elif sum(cards, one, two, user) < computerfinal(cone, ctwo, computer):
#     print("Try Again, You Loose")
# else:
#     print("Push")

import random

def deal_card(cards):
    card = random.choice(cards)
    return card

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
sumOfCardsOfUser = 0
user_cards = 0
computer_cards = 0
firstCardOfUser = int(deal_card(cards))
secondCardOfUser = int(deal_card(cards))
firstCardOfComputer = int(deal_card(cards))
secondCardOfComputer = int(deal_card(cards))
sumOfCardsOfUser = firstCardOfUser + secondCardOfUser
sumOfCardsOfComputer = 0
newCardQuestion = ""

def calculateComputerScore(sumOfCardsOfComputer, firstCardOfComputer, secondCardOfComputer):
    sumOfCardsOfComputer = firstCardOfComputer + secondCardOfComputer
    while sumOfCardsOfComputer < 17:
        sumOfCardsOfComputer+=int(deal_card(cards))
    print(f"The sum of cards of computer is {sumOfCardsOfComputer}")

def calculateScore(cards, sumOfCardsOfUser, firstCardOfUser, secondCardOfUser, sumOfCardsOfComputer, firstCardOfComputer):
    if sumOfCardsOfUser == 21:
        print("BlakcJack, You Win")
        return 0
    elif sumOfCardsOfUser > 21 and (firstCardOfUser == 11 or secondCardOfUser == 11):
        sumOfCardsOfUser-=10
        print(f"The sum of your cards is {sumOfCardsOfUser}")
        print(f"The first card of computer is {firstCardOfComputer}")
        newCardQuestion = input('Type "y" if you want another card or type "n" if you want to end the game')
        if newCardQuestion == "y":
            sumOfCardsOfUser+=int(deal_card(cards))
            calculateScore(cards, sumOfCardsOfUser, firstCardOfUser, secondCardOfUser, sumOfCardsOfComputer, firstCardOfComputer)
        elif newCardQuestion == "n":
            calculateComputerScore(sumOfCardsOfComputer, firstCardOfComputer, secondCardOfComputer)
            print({sumOfCardsOfComputer})
    elif sumOfCardsOfUser < 21:
        print(f"The sum of your cards is {sumOfCardsOfUser}")
        print(f"The first card of computer is {firstCardOfComputer}")
        newCardQuestion = input('Type "y" if you want another card or type "n" if you want to end the game')
        if newCardQuestion == "y":
            calculateScore(cards, sumOfCardsOfUser, firstCardOfUser, secondCardOfUser, sumOfCardsOfComputer, firstCardOfComputer)
        elif newCardQuestion == "n":
            calculateComputerScore(sumOfCardsOfComputer, firstCardOfComputer, secondCardOfComputer)
            print({sumOfCardsOfComputer})
    compare(sumOfCardsOfComputer, sumOfCardsOfUser)

def compare(sumOfCardsOfUser, sumOfCardsOfComputer):
    if sumOfCardsOfUser > 21:
        print("You Loose")
    elif sumOfCardsOfComputer > 21:
        print("You Win")
    elif sumOfCardsOfComputer == 21:
        print("Dealer gets Blackjack. You loose")
    elif sumOfCardsOfUser == 21:
        print("BLACKJACK!!!!!!!!!!!! YOU WIN")
    elif sumOfCardsOfUser > sumOfCardsOfComputer:
        print("Congratulations!!! You win")
    else:
        print("Push")

print(calculateScore(cards, sumOfCardsOfUser, firstCardOfUser, secondCardOfUser, sumOfCardsOfComputer, firstCardOfComputer))