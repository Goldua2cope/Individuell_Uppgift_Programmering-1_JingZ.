from Tjugoett import *
import sys, time

cards_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9' , 'J', 'Q', 'K', 'A' ]
card_suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

def main():
    # Iniate the deck, user and dealer as players
    the_deck = deck(cards_num, card_suits)
    the_user = player('Player')
    the_dealer = player('Dealer')

    # Users turn
    while not the_user.check_max_point():
        user_card = the_deck.deal_card()
        if user_card not in the_user.player_hand:
            the_user.to_hand_and_points(user_card)  
            print(the_user)
            time.sleep(1) 
            
        if the_user.check_max_point():
            break

        next_round_user = the_user.user_input('Do you want another card?')
        if next_round_user == 'yes':
            continue
        else:
            break

    if the_user.player_points == 21:
        print(f'You won! Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
        sys.exit()
    elif the_user.player_points > 21:
        print(f'You lost. Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
        sys.exit()

    # Dealers turn
    while not the_dealer.check_max_point():
        dealer_card = the_deck.deal_card()
        if dealer_card not in the_dealer.player_hand:
            the_dealer.to_hand_and_points(dealer_card)
            print(the_dealer)
            time.sleep(1) 

        if the_dealer.check_max_point():
            break

        next_round_dealer = the_dealer.dealer_choice()
        if next_round_dealer == 'yes':
            print('Dealer decides to draw a new card...')
            time.sleep(1)
            continue
        else:
            print('Dealer does not want to draw a new card...')
            break
    
    time.sleep(1)

    if the_dealer.player_points > 21 or the_dealer.player_points < the_user.player_points:
        print(f'You won! Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
    elif the_dealer.player_points == the_user.player_points:
        print(f'Draw! Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
    else:
        print(f'You lost. Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
        sys.exit()


if __name__=='__main__':
    main()