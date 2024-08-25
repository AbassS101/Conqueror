import random

suites = ["Flower", "Heart", "Spades", "Diamond"]
#values = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
values = ['A', 1, 2, 3, 4, 5, 6]
deck1 = [(card_suit, card_value) for card_suit in suites
         for card_value in values]
deck2 = [(card_suit, card_value) for card_suit in suites
         for card_value in values]

deck = deck1 + deck2
random.shuffle(deck)
players = []
print(deck)
numPlayers = int(input("How many players are playing: "))

for i in range(numPlayers):
  name = input(f"Enter the name of Player {i + 1}: ")
  hand = [deck.pop() for x in range(13)]
  players.append({"name": name, "hand": hand})


def showHand(player):
  print(f"{player['name']}'s hand: ")
  for i, (card_suit, card_value) in enumerate(player['hand']):
    print(f"{i + 1}: {card_suit} {card_value}")


def showDeck():
  for i, (card_suit, card_value) in enumerate(deck):
    print(f"{i + 1}: {card_suit} {card_value}")


discardPile = []


def grab(player, pile):
  if len(discardPile) != 0:
    x = discardPile.pop()
  y = deck.pop()
  if pile == "discard":
    player['hand'].append(x)
  elif pile == "deck":
    player['hand'].append(y)


def drop(player):
  showHand(player)
  x = int(input("Which card would you like to drop: "))
  dropped = player['hand'].pop(x - 1)
  discardPile.append(dropped)
  showHand(player)
  showDiscardPile()
  c = int(input("Do you have a winconditon(Order/Value/No): "))
  if (winCondition(player, c)):
    print(f"\n{player['name']} has won!!!")
    return True

def tempDrop(player):
  showHand(player)
  tempPile = []
  num = int(input("How many cards would you like to drop: "))
  for i in range(num):
      showHand(player)
      x = int(input("Which card would you like to drop: "))
      drops = player['hand'].pop(x-1)
      tempPile.append(drops)
  print("\nTemp Pile:\n")
  for i, (card_suit, card_value) in enumerate(tempPile):
    print(f"{i + 1}: {card_suit} {card_value}")
  return tempPile

def showDiscardPile():
  print("\nDiscard Pile:\n")
  for i, (card_suit, card_value) in enumerate(discardPile):
    print(f"{i + 1}: {card_suit} {card_value}")


def checkOrder(cards):
    # Ensure there are at least 3 cards
    if len(cards) < 3:
      return False
    # Define a dictionary to map card ranks to their numerical values
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for card_suit, card_value in cards:
        if card_value == 'A': 
          a = input("Do you want the Ace to be before 2 or after K(1/2): ")
          if a == "1":
            card_values['A'] = 1
    
    # Convert the input cards into their corresponding numerical values
    card_numerical_values = [card_values.get(card_value, 0) for card_suit, card_value in cards]

    # Check if the numerical values are in ascending order
    return all(card_numerical_values[i] <= card_numerical_values[i + 1] for i in range(len(card_numerical_values) - 1))

def winCondition(player, choice):
    cards = tempDrop(player)
    if choice == 1:
      return checkOrder(cards)
    elif choice == 2:
      print("hi")
    

turn = 0
cont = True
while cont:
  for currentPlayer in range(numPlayers):
    player = players[currentPlayer]
    print(f"\n{player['name']}'s turn.")
    showHand(player)
    v = input(
        "\n\nDo you want to grab from the deck or the discard pile(not available for the first player's first turn)? "
    )
    grab(player, v)
    if drop(player):
      cont = False
      break
    
    turn += 1
