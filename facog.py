# Wsp, so this is my first ever python game project, the idea came after i asked gemini for a mini beginner project, while most of the code here are
# Not AI assisted, i allowed Gemini to give me hints for codes i should use and actively encourage me to read python documentation.
# I will also be implementing the things i have learnt from Harvard's CS50p course

# Pls enjoy.         //CodeRPG//


def main():  # Main game

    weaponList = ["Sword"]
    consumableList = ["Health potion", "Bread", "Apple", "Pudding", "Bandage"]

    game_running = True  # Game can be switched to false which will stop the program if the user types in "Quit"
    inventory = ["Health potion", "Bread", "Sword"]
    health = int(100)
    gold = int(150)

    print("Welcome to the market game thingy mejiggy i have no fucking clue")
    print(
        "Choose what you want to use Numbers only, starts from 0, type in Shop to enter Shop"
    )

    while game_running:  # While loop, so the player can choose when to stop and also makes it that the game doesnt auto close after an input
        print("Inventory:   ", inventory)
        print("Gold:    ", gold)
        print("Health:  ", health)

        player_input = input()  # This is where the player can choose to use the items in the inventory or go to the shop or etc

        if player_input == "Shop":
            inventory, gold = shop_mechanic(inventory, gold)
        elif player_input.isdigit():
            intplayer_input = int(
                player_input
            )  # made a new player input varaible specifically to convert the given strings to integers (e.g, "123" -> 123)
            if intplayer_input < 0 or intplayer_input >= len(inventory):
                print("Out of range lil bro")
            else:
                print(inventory[intplayer_input])
                inventory, health = use_item(
                    intplayer_input, inventory, health, weaponList, consumableList
                )
        elif player_input == "Quit":
            print("Quitting")
            game_running = False
        elif player_input == "Fight":
            inventory, health, gold = fight_mechanic(
                inventory, health, gold, weaponList
            )


def use_item(
    player_input, inventory, current_health, weaponList, consumableList
):  # Once called, this function will take the player data and use the item according to the player input
    chosen_item = inventory[player_input]

    if chosen_item == "Health potion":
        print("*You gulp it down* yummy")
        heal = 25
        new_health = current_health + heal
        print("Healed by:   ", heal)
    elif chosen_item == "Bread":
        print("A bit stale but it will do i guess..")
        heal = 5
        new_health = current_health + heal
        print("Damaged by   :", heal)
    elif chosen_item == "Sword":
        print(
            "It's dull.."
        )  # This is just a placeholder code, Sword scripts coming soon
        new_health = current_health
    elif chosen_item == "Apple":
        print("*You eat the apple* crunchy")
        heal = 5
        new_health = current_health + heal
    elif chosen_item == "Pudding":
        print("Oo jiggly")
        heal = 12
        new_health = current_health + heal
    elif chosen_item == "Bandage":
        print("*You wrap the bandage on your wound*")
        heal = 20
        new_health = current_health + heal
    else:
        print("Out of range")

        new_health = current_health

    if chosen_item in consumableList:
        inventory.pop(
            player_input
        )  # Once the function is completed it will delete the chosen item, preventing it from being used again
    elif chosen_item in weaponList:
        inventory = inventory
    else:
        print("Item is not within a category")
        inventory = inventory

    return inventory, new_health  # Returns the updated player data to the caller


def shop_mechanic(
    inventory, gold
):  # Shop mechanic implemented, just add more codes later

    shop_inventory = ["Sword", "Apple", "Pudding", "Bandage"]
    print("Hello traveler, choose your item:    ", shop_inventory)

    price_list = {"Sword": 100, "Apple": 5, "Pudding": 15, "Bandage": 10}

    shop_input = input()

    if shop_input.isdigit():
        intshop_input = int(shop_input)
        if intshop_input < 0 or intshop_input >= len(shop_inventory):
            print("out of range (Choose within 0 - Length of shop inventory)")
            newgold = gold
            inventory = inventory
        else:
            chosen_item = shop_inventory[intshop_input]
            item_cost = price_list[chosen_item]

            print(f"Are you sure you would like to buy {chosen_item} for {item_cost}?")
            sureinput = str(input())
            if sureinput == "Y" or sureinput == "y":
                if gold >= item_cost:
                    print(f"{chosen_item} Purchased")
                    inventory.append(chosen_item)
                    newgold = gold - item_cost
                else:
                    print("Ur too broke buddy (fuck off peasant)")
                    inventory = inventory
                    newgold = gold
            elif sureinput == "N" or sureinput == "n":
                print("Purchase canceled my kind sir (Probably some homeless smh)")
                inventory = inventory
                newgold = gold
    else:
        print("Out of range")
        newgold = gold
        inventory = inventory

    return inventory, newgold


def fight_mechanic(
    inventory, health, gold, weaponList
):  # issues here, weaponList category not detected in the player's inventory despite having a weapon

    import random

    enemy = {"Goblin": 50, "Baby Goblin": 15}
    enemyarr = ["Goblin", "Baby Goblin"]

    for weapon in weaponList:
        if weapon in inventory:
            print("Are you sure you want to fight? (holy ur buff man)")
            startfight = str(input())
            if startfight == "Y" or startfight == "y":
                print("yoo ur fighting")
                random_enemy = random.choice(enemyarr)
                print(f"Theres a {random_enemy}!")
                # add more codes here later
            elif startfight == "N" or startfight == "n":
                print("Canceled (weakling)")
                inventory = inventory
                health = health
                gold = gold
            else:
                print("Out of range")
        elif weapon not in inventory:
            print("Buddy you can't fight without a weapon (lmao)")
            inventory = inventory
            health = health
            gold = gold
        else:
            print("Out of range (weirdo)")

    return inventory, health, gold


main()
