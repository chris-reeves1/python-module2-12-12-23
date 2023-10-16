#Sam has been dumped by his girlfriend so he's gone into the local milk 
#bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
#milkshakes, 
#differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
#number corresponding 
#to the relevant flavour - this list is displayed every iteration. 
#If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
#If he orders but can't pay he's thrown out.

budget = int(input("enter your budget: "))
shakes = {"1": 3, "2": 4, "3": 5}

while True:
    print("shake options: ")
    for option, price in shakes.items():
        print(f"{option}. ${price}")

    choice = input("what can i get you? (enter Q to quit): ")

    if choice.upper() == "Q":
        print("Goodbye!")
        break

    if choice not in shakes:
        print("invalid option") 
        continue

    price = shakes[choice]
    if price > budget:
        print("you cant afford that. Get out!")
        break
    
    print("enjoy your shake")
    budget -= price
    print(f"remaining budget: ${budget}")

