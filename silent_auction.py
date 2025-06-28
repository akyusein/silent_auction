from auction_art import logo
import getpass
import random
from items_for_auction import options


print(logo)
print("Welcome to this silent auction!")
pick = str(random.choice(options))
print(f"You're fighting to win {pick}! Good luck!\n")

def find_winner(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            winner = bidder["name"]
    print(f"\n🏆 {pick} goes to {winner} with a bid of £{highest_bid}!")
    return winner

def main():
    bidders = []
    bidding_open = True

    while bidding_open:
        name = input("What is your name? : ")
        bid = int(getpass.getpass(prompt='What is your bid?: £ ', stream=None))
        bidders.append({"name": name, "bid": bid})

        while True:
            more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
            if more_bidders == 'no':
                bidding_open = False
                break

            elif more_bidders == 'yes':
                break
            
            else:
                print("❌ Invalid input! Please type 'yes' or 'no'.\n")

    find_winner(bidders)

if __name__ == "__main__":
    main()