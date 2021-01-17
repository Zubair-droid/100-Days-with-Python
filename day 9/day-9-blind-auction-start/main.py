from replit import clear

from art import logo

print(logo)
#HINT: You can call clear() to clear the output in the console.
print("Welcome to the blind auction")
bids = {}
any_bidders = True
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while any_bidders:
 
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    bidders =  input("Is there any bidders to come? yes or no:")
    if bidders == "yes":
      clear()
    elif bidders == "no":
      any_bidders = False
      find_highest_bidder(bids)


