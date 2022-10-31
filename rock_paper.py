import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice=int(input("What do you choose? Type 0 for Rock,1 for paper or 2 for Scissors.")) 
if choice>=3:
    print("Invalid Choice!!")
image=[rock,paper,scissors]
print("YOU CHOSE:")
print(image[choice])
comp_action=random.randint(0,2)
print("COMPUTER CHOSE")
print(image[comp_action])
if choice==comp_action:
    print("TIED!!")      
elif choice==0:
    if comp_action==2:
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")
elif choice==1:
    if comp_action==0:
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")
elif choice==2:
    if comp_action==1:
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")            
       