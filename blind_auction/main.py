import os
from art import logo

def highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The highest bid was ${highest_bid}.\nCongratulations {winner.upper()}!!")


print(logo)

keep_going = True
bid_prices = {}

while keep_going:

    name = input("What's you name?: ")
    bid = int(input("What's your bid?: $"))

    bid_prices[name] = bid

    answer = input("Any other bid? ('yes' / 'no') ")

    if answer == "yes":
        keep_going = True
        os.system('cls')
    else:
        keep_going = False
        os.system('cls')
        highest_bid(bid_prices)
        




