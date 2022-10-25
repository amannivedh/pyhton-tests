print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name=name1+name2
l_name=name.lower()
t=l_name.count("t")
r=l_name.count("r")
u=l_name.count("u")
e=l_name.count("e")
true=t+r+u+e
l=l_name.count("l")
o=l_name.count("o")
v=l_name.count("v")
e=l_name.count("e")
love=l+o+v+e
truelove=str(true)+str(love)
if(int(truelove)<10)or(int(truelove)>90):
    print(f"Your score is {truelove},you go together like coke and mentos.")
elif(int(truelove)>=40)and(int(truelove)<=50):
    print(f"Your score is {truelove},you are alright together.")
else:
    print(f"Your score is {truelove}.")