import random
import pyinputplus as pyip

class deck():
    def __init__(self, cards_numeric, cards_suits):
        self.__cards_numeric = cards_numeric
        self.__cards_suits = cards_suits

    def __str__(self) -> str:
        return f'Available numeric values: {self.__cards_numeric}. Available suits: {self.__cards_suits}'

    def deal_card(self) -> str:
        return f'{random.choice(self.__cards_numeric)} {random.choice(self.__cards_suits)}'

class player():
    def __init__(self, name : str) -> None:
        self.name = name
        self.player_points = 0
        self.player_hand = []
        self.max_points = 21
        # self.deck_instance : deck_instance

    def __str__(self) -> str:
        return f"""Current points for {self.name}: {self.player_points}. 
        Current hand for {self.name}: {'No cards.' if not self.player_hand else ','.join(self.player_hand)}."""
    
    def card_to_points(self, card : str) -> int:
        card_value = card.split()[0]
        if card_value.isdigit():
            return int(card_value)
        elif card_value == 'J':
            return 10
        elif card_value == 'Q':
            return 11
        elif card_value == 'K':
            return 12
        elif card_value == 'A':
            return self.ace_value()

    @staticmethod
    def ace_value() -> int:
        return pyip.inputNum(prompt='Do you want your ace to have the value 1 or 14?\n', choices=[1, 14])
        # while True:
        #     user_choice = pyip.inputNum(prompt='Do you want your ace to have the value 1 or 14?\n')
        #     if user_choice in [1, 14]:
        #         return user_choice
        #     else:
        #         print('Invalid input')
        #         continue

    # Completion of one round for the user:
    # saves received card in player_hand, converts card to points and saves in player_points
    def to_hand_and_points(self, card: str) -> None:
        self.player_hand.append(card)
        self.player_points += self.card_to_points(card)
        print(f'{self.name} has received {card}.')
        

    @staticmethod
    def user_input(prompt : str) -> str:
        return pyip.inputYesNo(prompt=prompt + '\n')
    
    @staticmethod
    def dealer_choice() -> str:
        return random.choice(['yes', 'no'])

    def check_max_point(self) -> bool:
        return self.player_points >= self.max_points

    
