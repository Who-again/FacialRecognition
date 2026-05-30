#Wsp, so this is my first ever python game project, the idea came after i asked gemini for a mini beginner project, while most of the code here are
#Not AI assisted, i allowed Gemini to give me hints for codes i should use and actively encourage me to read python documentation.
#I will also be implementing the things i have learnt from Harvard's CS50p course

#Pls enjoy.         //CodeRPG//



def main(): #Main game
    game_running = True     #Game can be switched to false which will stop the program if the user types in "Quit"
    inventory = ["Health potion", "Bread"]
    health = int(100)
    gold = int(1000)

    print("Welcome to the market game thingy mejiggy i have no fucking clue")
    print("Choose what you want to use Numbers only, starts from 0, type in Shop to enter Shop")

    while game_running:     #While loop, so the player can choose when to stop and also makes it that the game doesnt auto close after an input
        print("Inventory:   ", inventory)
        print("Gold:    ", gold)
        print("Health:  ", health)

        player_input = input()      #This is where the player can choose to use the items in the inventory or go to the shop or etc
        
        if player_input == "Shop":
            inventory, gold = shop_mechanic(inventory, gold)
        elif player_input .isdigit():
            intplayer_input = int(player_input)     #made a new player input varaible specifically to convert the given strings to integers (e.g, "123" -> 123)
            if intplayer_input < 0 or intplayer_input >= len(inventory):
                print("Out of range lil bro")
            else:
                print(inventory[intplayer_input])
                inventory, health = use_item(intplayer_input, inventory, health)
        elif player_input == "Quit":
            print("Quitting")
            game_running = False

def use_item(player_input, inventory, current_health):  #Once called, this function will take the player data and use the item according to the player input
    chosen_item = inventory[player_input]

    if chosen_item == "Health potion":
        heal = 25
        new_health = current_health + heal
        print("Healed by:   ",heal)
    elif chosen_item == "Bread":
        print("Why does it taste like dog shit wrapped in cat shit..")
        damage = 5
        new_health = current_health - damage
        print("Damaged by   :", damage)
    else:
        print("Out of range")
        new_health = current_health
    inventory.pop(player_input)     #Once the function is completed it will delete the chosen item, preventing it from being used again
    return inventory, new_health    #Returns the updated player data to the caller

def shop_mechanic(inventory, gold):     # Shop mechanic implemented, just add more codes later

    shop_inventory = ["Sword", "Apple", "Pudding", "Bandage"]
    print("Hello traveler, choose your item:    ",shop_inventory)
    
    shop_input = int(input())
    chosen_item = shop_inventory[shop_input]

    SwordCost = 100
    AppleCost = 5
    PuddingCost = 15
    BandageCost = 10

    if chosen_item == "Sword":
        print(f"Are you sure you wnat to buy {chosen_item} for {SwordCost}?")
        sureinput = str(input())
        if sureinput == "Y":
            print(f"{chosen_item} bought")
            inventory.append(chosen_item)
            newgold = gold - SwordCost
            return inventory, newgold

main()
    