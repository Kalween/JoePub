import random
import art

deck_of_cards = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

def start_deal():
    player = []
    computer = []
    for i in range(2):
        player.append(random.choice(list(deck_of_cards.values())))
    computer.append(random.choice(list(deck_of_cards.values())))
    return player, computer

def play_again():
    return input("Would you like to play again? (y/n): ").lower() == 'y'

def determine_winner(player, computer):
    player_score = sum(player)
    computer_score = sum(computer)
    if player_score > 21:
        return "Player busts. Computer wins!"
    elif computer_score > 21:
        return "Computer busts. Player wins!"
    elif player_score > computer_score:
        return "Player wins!"
    elif player_score < computer_score:
        return "Computer wins!"
    else:
        return "It's a tie!"

def main():

    while True:
        print(art.logo)
        player, computer = start_deal()
        while True:
            print(f"Your cards: {player}. Current Score: {sum(player)}")
            print(f"Computer's first card: {computer[0]}")
            hit_or_stop = input("Type 'hit' to get another card, or 'stop' to stop: ").lower()
            if hit_or_stop == 'hit':
                player.append(random.choice(list(deck_of_cards.values())))
                if sum(player) > 21 and 11 not in player:
                    print(f"You bust. {sum(player)}")
                    break
                elif sum(player) > 21 and 11 in player:
                    index_of_ace = player.index(11)  # Find the index of the Ace
                    player[index_of_ace] = 1  # Replace the value of the Ace from 11 to 1
            else:
                while sum(computer) <= 17:
                    computer.append(random.choice(list(deck_of_cards.values())))
                    if sum(computer) >21 and 11 in computer:
                        index_of_ace = computer.index(11)
                        computer[index_of_ace] = 1
                print(f"Your final hand: {player}. Your final score: {sum(player)}")
                print(f"Computer's final hand: {computer}. Computer's final score: {sum(computer)}")
                print(determine_winner(player, computer))
                break

        if not play_again():
            print("Goodbye!")
            break
        else:
            continue

if __name__ == "__main__":
    main()