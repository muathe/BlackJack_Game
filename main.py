import random
from replit import clear


def deck():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate(card):
  if sum(card) == 21 and len(card) == 2:
    return 0

  if 11 in card and sum(card) > 21:
    card.remove(11)
    card.append(1)

  return sum(card)


def compare(user_score, computer_score):

  if user_score > 21 and computer_score > 21:
    return "You Lose!"

  elif user_score == computer_score:
    return "Its a Tie!"

  elif user_score == 0:
    return "BlackJack!"

  elif computer_score == 0:
    return "You Lose"

  elif user_score > 21:
    return "You lose!"

  elif computer_score > 21:
    return "You win!"

  elif user_score > computer_score:
    return "You Win!"

  else:
    return "You Lose!"


def play_game():
  
  user_cards = []
  computer_cards = []
  game_over = False

  for x in range(2):
    user_cards.append(deck())
    computer_cards.append(deck())

  while game_over != True:
  
    user_score = calculate(user_cards)
    computer_score = calculate(computer_cards)

    print(f"User score: {user_score}, User cards: {user_cards}")
    print(f"Computer card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:

      ask = input("Would you like another card? 'y' or 'n': ")
      if ask == "y":
        user_cards.append(deck())
      else:
        game_over = True
        

      
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deck())
    computer_score = calculate(computer_cards)
    
  print(f"Final score: {user_score}, Final hand: {user_cards}")
  print(f"Computer final score: {computer_score}, Computer's final hand: {computer_cards}")
  print(compare(user_score, computer_score))

while input("Would you like to play a game of BlackJack? ") == "y":
  clear()
  play_game()






#Code Block 79
