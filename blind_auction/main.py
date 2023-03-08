import os
from art import logo

def add_new_bid(participant_name, bid_price):
    new_bid = {}
    new_bid["name"] = participant_name
    new_bid["bid"] = bid_price
    bid_prices.append(new_bid)

print(logo)

bid_prices = []
keep_going = True
highest_bid = 0

while keep_going:

    name = input("What's you name?: ")
    bid = int(input("What's your bid?: $"))

    if bid > highest_bid:
        winner = name
        highest_bid = bid

    add_new_bid(name, bid)

    answer = input("Any other bid? ('yes' / 'no') ")

    if answer == "yes":
        keep_going = True
        os.system('cls')
    else:
        keep_going = False
        
os.system('cls')
print(f"The highest bid was ${highest_bid}.\nCongratulations {winner.upper()}!!")


