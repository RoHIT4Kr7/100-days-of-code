print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first_input= input("You're at a cross road. where do you want to go? Type 'left' or 'right' ")
if(first_input=="left"):
    print('You come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. type "swim" to swim across')
    second_input=input()
    if(second_input=="wait"):
        print("You arrive at the island unharmed. there is a house with 3 doors. One red, One yellow and one blue. which colour do you choose?")
        third_input=input()
        if(third_input=="yellow"):
            print("You Win")
        elif third_input in ["red", "blue"]:
            print("Eaten by beasts. Game Over.")
    elif(second_input=="swim"):
        print("Attacked by trout. Game over")
else:
    print("Fall into a hole Game Over")