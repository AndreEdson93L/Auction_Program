from replit import clear
from art import logo

print(logo)
print('Welcome to the secret auction program.')

there_is_a_bidder = True
bidders = {}

def add_new_bidder(dictionary,name_key, bid_value):
  dictionary[name_key] = bid_value

def find_highest_bidder(bidding_record):
 real_max = 0
 highest_bidder = ''
 for key in bidding_record:
   search_max = bidding_record[key]
   if search_max > real_max:
     real_max = int(search_max)
     highest_bidder = key

 print(f"The highest bidder is {highest_bidder} with a bid of ${real_max}")

while there_is_a_bidder:
  name = input('What is your name? ')
  bid = float(input("What's your bid? $"))
  add_new_bidder(bidders, name, bid)
  new_bid = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
  if new_bid == 'no':
    find_highest_bidder(bidders)
    there_is_a_bidder = False
  elif new_bid == 'yes':
    clear()
