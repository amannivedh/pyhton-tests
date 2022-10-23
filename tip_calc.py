print("Welcome to Tip Calculator")
bill=float(input("\nwhat is the total bill?"))
x=int(input("\nwhat percentage tip would you like to give?"))
percent=x/100
tip=percent*bill
total=bill+tip
div=int(input("\nhow many people to split the bill?"))
each=total/div
print(f"each must pay {each}")
