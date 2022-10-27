print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("___WELCOME TO TREASURE ISLAND___")
print("\nYour mission is to find the treasure")
choice1=input("\nYou are at a crossroad..choose your path, LEFT or RIGHT\n").lower()
if choice1=="left":
    choice2=input("\nYou have arrived at a river...will you SWIM across or WAIT for a boat?").lower()
    if choice2=="wait":
        choice3=input("\nYou reached the island safely...and see 3 doors RED YELLOW and BLUE..choose one door\n").lower()
        if choice3=="red":
            print("\nYou entered a room of fire...GAME OVER!!")
        elif choice3=="yellow":
            print("\nCONGRATULATIONS..YOU HAVE FOUD THE TREASURE!!")
        elif choice3=="blue":
            print("\nYou have arrived into a room of HUNGRY BEASTS...GAME OVER!!")
        else:
            print("\nYou chose a door that doesnt exist...GAME OVER!!")
    else:
        print("\nYou are attacked by a group of hungry trouts...GAME OVER!!")
else:
    print("\nYou fell into a ditch...GAME OVER!!")