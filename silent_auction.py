bids={}         
bidding_finished=False

def  find_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amt=bidding_record[bidder]
        if bid_amt>highest_bid:
            highest_bid=bid_amt
            winner=bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")        
    exit()    

def continue_bidding():                 
    name=input("wWat is your name?")
    price=int(input("What is your bid? $"))
    bids[name]=price
    should_continue=input("Are there any other Bidders? Type 'yes' or 'no'.").lower()
    if should_continue=="no":
        bidding_finished=True
        find_bidder(bids)
    elif should_continue=="yes":
        continue_bidding()

while not bidding_finished:
    continue_bidding()        