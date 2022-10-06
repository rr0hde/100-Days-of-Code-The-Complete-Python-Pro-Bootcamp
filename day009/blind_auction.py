from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.
print(logo)

print("Welcome to the secret auction program.\n")

bids = {}
keepBidding = True


def winner(bidRecord):
    maxBid = 0
    maxBidder = ''
    for bidder in bidRecord:
        bidAmount = bidRecord[bidder]
        print(bidAmount)
        if bidAmount > maxBid:
            maxBid = bidAmount
            maxBidder = bidder
    print(f"The winner is {maxBidder} with a bid of ${maxBid}.")


while keepBidding:
    newDict = {}
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    cont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if cont == 'yes':
        clear()
    else:
        keepBidding = False
        winner(bids)
