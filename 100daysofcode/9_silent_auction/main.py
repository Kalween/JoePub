import os

more_bids = True
auctioneer = []

def add_person(name,bid):
    new_bidder = {"name":name, "bid":bid}
    auctioneer.append(new_bidder)

def find_highest_bidder():
    highest_bid = 0
    winner = ""
    for bidder in auctioneer:
        bid_amount = bidder["bid"]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder["name"]
    print(f"The winner is {winner} with the highest bid of {highest_bid}")
while more_bids is True:
    name = input("What is your name?: ")
    bid = int(input("how much would you like to bid?: $ "))
    add_person(name, bid)
    question = input("Are there any more who would like to bid? ")
    if question == 'yes':
        os.system('clear')
    elif question == 'no':
        os.system('clear')
        find_highest_bidder()
        more_bids = False
    else:
        print("Wrong syntax, try again")