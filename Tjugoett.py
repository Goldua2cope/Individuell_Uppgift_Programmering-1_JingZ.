import random
import pyinputplus as pyip

class deck():
    # Initiate attributes for the deck
    def __init__(self, cards_numeric : tuple, cards_suits : tuple):
        self.cards_numeric = cards_numeric
        self.cards_suits = cards_suits

    def __str__(self) -> str:
        return f'Available numeric values: {self.cards_numeric}. Available suits: {self.cards_suits}'

    # Method to generate a random card
    def deal_card(self) -> str:
        return f'{random.choice(self.cards_numeric)} {random.choice(self.cards_suits)}'

# Parent class
class player():
    max_points : int = 21
    # Initiate attribute for player objects
    def __init__(self, name : str) -> None:
        self.name = name
        self.player_points : int = 0
        self.player_hand : list = []

    def __str__(self) -> str:
        return f"""Current points for {self.name}: {self.player_points}. 
        Current hand for {self.name}: {'No cards.' if not self.player_hand else ','.join(self.player_hand)}."""
    
    # Method to monitor if player points is equal or exceed the limit 21
    def check_max_point(self) -> bool:
        return self.player_points >= player.max_points

# Child class for user
class user(player):
    def __init__(self, name : str) -> None:
        super().__init__(name)

    # Method to return the value of a card where user can choose value of 'Ace'
    def card_to_points(self, card : str) -> int:
        card_value : str = card.split()[0]
        if card_value.isdigit():
            return int(card_value)
        elif card_value == 'J':
            return 10
        elif card_value == 'Q':
            return 11
        elif card_value == 'K':
            return 12
        elif card_value == 'Ace':
            return self.ace_value('Do you want your ace to have the value 1 or 14?')
        
    # Method to handle the value of 'Ace'
    @staticmethod
    def ace_value(text : str) -> int:
        while True:
            user_choice = pyip.inputNum(prompt = text + '\n')
            if user_choice in [1, 14]:
                return user_choice
            else:
                print('Value must be 1 or 14!')

    # adds card to users hand, converts card to points and adds to user_points
    def save_card_and_points_dealer_user(self, card: str) -> None:
        self.player_hand.append(card)
        print(f'{self.name} received {card}.')
        self.player_points += self.card_to_points(card)

    # Method used to ask user if they want another card
    @staticmethod
    def user_input(prompt : str) -> str:
        # pyip.inputYesNo handles all ValueErrors
        return pyip.inputYesNo(prompt=prompt + '\n')

# Child class for computer as dealer
class dealer(player):
    def __init__(self, name : str) -> None:
        super().__init__(name)

    # Method to return the value of a card with computer simulation
    def card_to_points_simulation(self, card : str) -> int:
        card_value : str = card.split()[0]
        if card_value.isdigit():
            return int(card_value)
        elif card_value == 'J':
            return 10
        elif card_value == 'Q':
            return 11
        elif card_value == 'K':
            return 12
        elif card_value == 'Ace':
            return random.choice([1, 14])
    
    # adds card to dealers hand, converts card to points and adds to dealer_points
    def save_card_and_points_dealer(self, card: str) -> None:
        self.player_hand.append(card)
        print(f'{self.name} received {card}.')
        self.player_points += self.card_to_points_simulation(card)
    
    # Method to simulate dealers choice
    @staticmethod
    def dealer_choice() -> str:
        return random.choice(['yes', 'no'])
