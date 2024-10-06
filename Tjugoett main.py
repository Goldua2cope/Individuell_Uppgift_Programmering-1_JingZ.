from Tjugoett import *
import sys, time

cards_num : tuple = ('1', '2', '3', '4', '5', '6', '7', '8', '9' , 'J', 'Q', 'K', 'Ace')
card_suits : tuple = ('Clubs', 'Spades', 'Hearts', 'Diamonds')

def main():
    # Initiate the deck, user and dealer as players
    the_deck : object = deck(cards_num, card_suits)
    the_user : object = user('Player')
    the_dealer : object = dealer('Dealer')

    # Welcome phrase
    print(' Welcome to Tjugoett! '.center(40, '='))
    print('')

    # Users turn when users points < 21
    while not the_user.check_max_point():
        # Deals card to user
        user_card = the_deck.deal_card()
        print('')
        # saves card to users hand, adds cards value to users points
        if user_card not in the_user.player_hand:
            the_user.save_card_and_points_dealer_user(user_card)  
            print(f'{the_user}\n')
            time.sleep(1) 
        # makes sure a new card is generated
        else:
            continue
        
        # Checks if user points is equal to or exceeds 21
        if the_user.check_max_point():
            break

        # Ask if user wants another card 
        if the_user.user_input('Do you want another card? (y/n)') == 'yes':
            continue
        else:
            break

    # Checks winning and loosing conditions for users points
    if the_user.player_points == 21:
        print(f'You won! Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
        sys.exit()
    elif the_user.player_points > 21:
        print(f'You lost. Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
        sys.exit()

    # Dealers turn when dealers points < 21 and users winning/losing condition is not met 
    while not the_dealer.check_max_point():
        # Deals card to dealer
        dealer_card = the_deck.deal_card()
        print('')
        # Adds card to dealers hand, saves cards value as dealers points
        if dealer_card not in the_dealer.player_hand:
            the_dealer.save_card_and_points_dealer(dealer_card)
            print(f'{the_dealer}\n')
            time.sleep(1) 
        # Makes sure a new card is generated
        else:
            continue

        # Checks if dealers points is equal to or exceeds 21
        if the_dealer.check_max_point():
            break

        # Simulates if dealer wants to draw another card
        if the_dealer.dealer_choice() == 'yes':
            print('Dealer decides to draw a new card...')
            time.sleep(1)
            continue
        else:
            print('Dealer does not want to draw a new card...')
            break
    
    time.sleep(1)

    # Compares dealers and users points and checks winning conditions
    if the_dealer.player_points > 21 or the_dealer.player_points < the_user.player_points:
        print(f'You won! Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
    elif the_dealer.player_points == the_user.player_points:
        print(f'Draw! Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
    else:
        print(f'You lost. Your points: {the_user.player_points}. Dealers points: {the_dealer.player_points}')
    
    sys.exit()


if __name__=='__main__':
    main()
