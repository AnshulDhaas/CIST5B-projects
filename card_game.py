#Group 5: Anshul, Riya, and Rajveer

#Node, Card, Player and Deck done by Anshul
#UnitCard and SpellCard  done by Riya and Anshul
#GameState/Game Logic done by Rajveer

import random

#Node class for linked list implementation of deck
class Node:
    def __init__(self, card):
        self.card = card
        self.next = None

class Card:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost

    def __str__(self):
        return f"{self.name} - {self.description} (Cost: {self.cost})"
#UnitCard and SpellCard classes inheriting from Card
class UnitCard(Card):
    def __init__(self, name, description, cost, attack, hp):
        super().__init__(name, description, cost)
        self.attack = attack
        self.hp = hp

    def attack_opponent(self, opponent_unit):
        opponent_unit.hp -= self.attack
        print(f"{self.name} attacks {opponent_unit.name} for {self.attack} damage!")
        if opponent_unit.hp <= 0:
            print(f"{opponent_unit.name} is defeated!")
        else:
            print(f"{opponent_unit.name} has {opponent_unit.hp} HP left.")

class SpellCard(Card):
    def __init__(self, name, description, cost, effect):
        super().__init__(name, description, cost)
        self.effect = effect
    
    def cast(self, target_player):
        if "damage" in self.effect:
            damage = int(self.effect.split(" ")[1])
            target_player.hp -= damage
            print(f"{self.name} deals {damage} damage to {target_player.name}!")
        elif "heal" in self.effect:
            heal = int(self.effect.split(" ")[1])
            target_player.hp += heal
            print(f"{self.name} heals {target_player.name} for {heal} HP!")
        else:
            print(f"Spell {self.name} has an unknown effect: {self.effect}")

# Deck class using Linked List
class Deck:
    def __init__(self):
        self.head = None  # The top of the deck
        self.tail = None  # The bottom of the deck
        self.size = 0     # # of cards in the deck
    
    def add_card(self, card): #add card to the deck
        new_node = Node(card)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def draw_card(self): #draw card from deck
        if self.head:
            drawn_card = self.head.card
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return drawn_card
        else:
            return None
    
    def shuffle(self): #shuffle the deck
        cards = []
        current = self.head
        while current:
            cards.append(current.card)
            current = current.next

        # Shuffle the cards
        random.shuffle(cards)

        # Re-initialize the linked list
        self.head = None
        self.tail = None
        self.size = 0
        for card in cards:
            self.add_card(card)

# Player class with deck and hand
# Aggregation: Player has a Deck and a list of Cardd objects in their hand and played units. This is another example of aggregation where Player is composed of a Dec and lists of Card objects.
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.deck = Deck()
        self.hand = []
        self.played_units = []

    def draw_card(self): #draw card from deck as a player
        card = self.deck.draw_card()
        if card:
            self.hand.append(card)
            print(f"{self.name} draws {card.name}")
        else:
            print(f"{self.name}'s deck is empty!")
    
    def play_card(self, game_state):  # play card from linked list deck
        while True:
            try:
                # Show hand and ask for a valid input
                self.show_hand()
                card_index = int(input(f"{self.name}, choose a card index to play (0 to skip): "))
                
                if card_index == 0:
                    print(f"{self.name} chose to skip playing a card.")
                    break  # Skip playing a card this turn

                # Adjust for 1-based index input (user sees 1 as first card)
                if card_index < 1 or card_index > len(self.hand):
                    raise ValueError("Invalid card index!")

                # Adjust the index for 0-based indexing
                card = self.hand.pop(card_index - 1)  
                
                if isinstance(card, UnitCard):
                    # Play the unit card to the field
                    self.played_units.append(card)
                    print(f"{self.name} plays {card.name} (Unit Card: {card.attack} ATK / {card.hp} HP)")
                elif isinstance(card, SpellCard):
                    # Cast the spell
                    opponent = game_state.get_opponent(self)
                    card.cast(opponent)
                    print(f"{self.name} casts {card.name} (Spell Card)")
                
                break  # Exit loop once a valid card is played

            except ValueError as e:
                print(f"Error: {e}. Please try again.")
    
    def attack_with_units(self, game_state): #attack with units
        opponent = game_state.get_opponent(self)
        for unit in self.played_units:
            if opponent.played_units:
                # Attack the first unit of the opponent
                unit.attack_opponent(opponent.played_units[0])
                if opponent.played_units[0].hp <= 0:
                    opponent.played_units.pop(0)  # Remove defeated unit
            else:
                # Attack opponent directly if no units are on the field
                opponent.hp -= unit.attack
                print(f"{self.name}'s {unit.name} attacks {opponent.name} directly for {unit.attack} damage!")
                if opponent.hp <= 0:
                    print(f"{opponent.name} is defeated!")
                    break
    def show_hand(self): #show hand of the player
        if not self.hand:
            print(f"{self.name} has no cards in hand.") 
        else:
            for i, card in enumerate(self.hand): # Enumerate to iterate over the list and return the index and the value
                print(f"{i + 1}: {card}")

# GameState class to track the game state
#- GameStat has associations with Player objects. It has two Player objects.
class GameState:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.log = []
    
    
    def log_action(self, action): #Action log of players
        self.log.append(action)
        print(action)
    
    def check_winner(self): #Check winner of the game
        if self.player1.hp <= 0:
            return f'{self.player2.name} wins!'
        elif self.player2.hp <= 0:
            return f'{self.player1.name} wins!'
        return None

    def get_opponent(self, current_player):
        return self.player2 if current_player == self.player1 else self.player1

# Game loop
def play_game():
    # Initialize players
    player1 = Player("Player 1", 20)
    player2 = Player("Player 2", 20)
    
    # Initialize the game
    game_state = GameState(player1, player2)
    
    # Add cards to each player's deck
    player1.deck.add_card(UnitCard("Unit 1", "Berserk", cost=2, attack=3, hp=4))
    player1.deck.add_card(UnitCard("Unit 2", "Knight", cost=2, attack=3, hp=4))
    player1.deck.add_card(UnitCard("Unit 3", "King", cost=2, attack=3, hp=4))
    player1.deck.add_card(UnitCard("Unit 4", "Battle Ram", cost=2, attack=3, hp=4))
    player1.deck.add_card(UnitCard("Unit 5", "Barbarian", cost=2, attack=3, hp=4))
    
    player1.deck.add_card(SpellCard("Spell 1", "Fireball", cost=3, effect="deal 5 damage"))
    player1.deck.add_card(SpellCard("Spell 2", "Poison", cost=3, effect="deal 5 damage"))
    player1.deck.add_card(SpellCard("Spell 3", "Lightning", cost=3, effect="deal 5 damage"))
    player1.deck.add_card(SpellCard("Spell 4", "Blizzard", cost=3, effect="deal 5 damage"))
    player1.deck.add_card(SpellCard("Spell 5", "Meteor", cost=3, effect="deal 5 damage"))
    
    player2.deck.add_card(UnitCard("Unit 1", "Berserk", cost=2, attack=3, hp=4))
    player2.deck.add_card(UnitCard("Unit 2", "Knight", cost=2, attack=3, hp=4))
    player2.deck.add_card(UnitCard("Unit 3", "King", cost=2, attack=3, hp=4))
    player2.deck.add_card(UnitCard("Unit 4", "Battle Ram", cost=2, attack=3, hp=4))
    player2.deck.add_card(UnitCard("Unit 5", "Barbarian", cost=2, attack=3, hp=4))
    
    player2.deck.add_card(SpellCard("Spell 1", "Fireball", cost=3, effect="deal 5 damage"))
    player2.deck.add_card(SpellCard("Spell 2", "Poison", cost=3, effect="deal 5 damage"))
    player2.deck.add_card(SpellCard("Spell 3", "Lightning", cost=3, effect="deal 5 damage"))
    player2.deck.add_card(SpellCard("Spell 4", "Blizzard", cost=3, effect="deal 5 damage"))
    player2.deck.add_card(SpellCard("Spell 5", "Meteor", cost=3, effect="deal 5 damage"))

    # Shuffle both decks
    player1.deck.shuffle()
    player2.deck.shuffle()

    # Players draw initial hands (5 cards)
    for _ in range(5):
        player1.draw_card()
        player2.draw_card()

    # Main game loop
    while not game_state.check_winner():
        # Player 1's turn
        print("\nPlayer 1's turn")
        player1.draw_card()
        player1.play_card(game_state)  # Call the new play_card method

        if game_state.check_winner():
            break

        # Player 2's turn
        print("\nPlayer 2's turn")
        player2.draw_card()
        player2.play_card(game_state)  # Call the new play_card method

    print(f"The winner is {game_state.check_winner()}!")

# Run the game
play_game()
'''
Relationships:

- Inheritance:
  - UnitCard -> Card
  - SpellCard -> Card

- Aggregation:
  - Player` -> Deck
  - Player -> List of Card (hand and played units)
  
- Composition:
  - Deck -> Node -> Card

- Association:
  - GameState -> Player
'''


