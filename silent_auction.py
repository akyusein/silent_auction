from auction_art import logo
import getpass
import random
from items_for_auction import options

print(logo)
print("Welome to this silent auction!")
pick = str(random.choice(options))
print(f"You're fighting to win {pick}! Good luck!")


def main():
    bidders = []
    bidding_open = True

    while bidding_open:
        name = input("What is your name? : ")
        bid = int(getpass.getpass(prompt='What is your bid?: £ ', stream=None))
        bidders.append({"name": name, "bid": bid})
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

        if more_bidders == 'no':
            bidding_open = False
            find_winner(bidders)

def find_winner(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            winner = bidder["name"]
        
    print(f"{pick} goes to {winner} with a bid of £{highest_bid}")
    return winner
    
if __name__ == "__main__":
    main()
