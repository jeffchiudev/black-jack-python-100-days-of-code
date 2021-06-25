from art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  """Returns random card from deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  dealt_card = random.choice(cards)
  return dealt_card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calc_score(cards):
  """takes list of cards and calculate score"""
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) ==2:
    return 0
  
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, dealer_score):
  if user_score == dealer_score:
    return "Draw"
  elif dealer_score == 0:
    return "Dealer wins"
  elif user_score == 0:
    return "You Win!"
  elif user_score > 21:
    return "Bust, you lose."
  elif dealer_score > 21:
    return "Dealer busts, you win!"
  elif user_score > dealer_score: 
    return "You win!"
  else:
    return "You lose"

def play_game():

  print(logo)
  
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  dealer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while not game_over: 
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calc_score(user_cards)
    dealer_score = calc_score(dealer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Dealer's first card: {dealer_cards[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
      game_over = True
    else: 
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calc_score(dealer_cards)

  print(f"  Your final hand: {user_cards}, your score: {user_score}")
  print(f"  Dealer final hand: {dealer_cards}, dealer score: {dealer_score}")
  print(compare(user_score, dealer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Would you like to play a game of Blackjack? Type 'y'  or 'n': ") == "y":
  play_game()