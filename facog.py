# Wsp, so this is my first ever python game project, the idea came after i asked gemini for a mini beginner project, while most of the code here are
# Not AI assisted, i allowed Gemini to give me hints for codes i should use and actively encourage me to read python documentation.
# I will also be implementing the things i have learnt from Harvard's CS50p course

# Pls enjoy.         //CodeRPG//
import json


def load_game():  # took me a few hours to learn these JSON stuff, war is over boys YOOHOOOOOOOO
    try:
        with open("player_data.json", "r") as file:
            loaded_data = json.load(file)
            return loaded_data["inventory"], loaded_data["health"], loaded_data["gold"]
    except FileNotFoundError:  # By default, if there's no player data the program will generate one for you and give you the standard kit
        print("No player data, generating..")

        default_data = {
            "inventory": ["Bread", "Health Potion"],
            "health": 100,
            "gold": 150,
        }

        with open("player_data.json", "w") as file:
            json.dump(default_data, file, indent=4)
            print("Generated!")

        return ["Bread", "Health Potion"], 100, 150


def save_game(inventory, health, gold):
    save_list = {"inventory": inventory, "health": health, "gold": gold}

    with open("player_data.json", "w") as file:
        json.dump(save_list, file, indent=4)
        print("Saving...")


def main():  # Main game

    weaponList = ["Sword", "Axe"]
    consumableList = ["Health potion", "Bread", "Apple", "Pudding", "Bandage"]
    # pls add one more category for selling items, i recently added goblin flesh and goblin eyes as lootdrop, i might just create like a valuable category that i can use to sell stuff

    game_running = True  # Game can be switched to false which will stop the program if the user types in "Quit"

    inventory, health, gold = load_game()

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
            save_game(inventory, health, gold)
            game_running = False

        elif player_input == "Fight" or player_input == "fight":
            inventory, health, gold = fight_mechanic(
                inventory, health, gold, weaponList, consumableList
            )


def use_item(
    player_input, inventory, current_health, weaponList, consumableList
):  # Once called, this function will take the player data and use the item according to the player input
    chosen_item = inventory[player_input]

    if chosen_item == "Health potion":
        print("*You gulp it down* yummy")
        heal = 25
        new_health = current_health + heal
    elif chosen_item == "Bread":
        print("A bit stale but it will do i guess..")
        heal = 5
        new_health = current_health + heal
    elif chosen_item == "Sword":
        print(
            "It's dull.."
        )  # This is just a placeholder code, Sword scripts coming soon. EDIT: there's a fight mechanic now! :D
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
        pass
    else:
        print("Item is not within a category")

    if new_health > 100:
        new_health = 100

    return inventory, new_health  # Returns the updated player data to the caller


def shop_mechanic(inventory, gold):

    sell_list = {"Goblin Eyes": 50, "Goblin Flesh": 35}
    price_list = {"Sword": 100, "Apple": 5, "Pudding": 15, "Bandage": 10}
    shop_inventory = list(price_list.keys())
    print("Hello traveler, choose your item:    ", shop_inventory)

    shop_input = input()

    if shop_input.isdigit():
        intshop_input = int(shop_input)

        if intshop_input < 0 or intshop_input >= len(shop_inventory):
            print("out of range (Choose within 0 - Length of shop inventory)")
        else:
            chosen_item = shop_inventory[intshop_input]
            item_cost = price_list[chosen_item]
            print(f"Are you sure you would like to buy {chosen_item} for {item_cost}?")
            sureinput = str(input())

            if sureinput == "Y" or sureinput == "y":
                if gold >= item_cost:
                    print(f"{chosen_item} Purchased")
                    inventory.append(chosen_item)
                    gold -= item_cost

                else:
                    print("Ur too broke buddy (fuck off peasant)")
            elif sureinput == "N" or sureinput == "n":
                print("Purchase canceled my kind sir (Probably some homeless smh)")
    elif shop_input == "Sell" or shop_input == "sell":
        print("What would you like to sell?")
        print(inventory)
        intsell_input = input()
        if intsell_input.isdigit():
            intsell_input = int(intsell_input)
            if intsell_input < 0 or intsell_input >= len(inventory):
                print("out of range (stupid)")
            else:
                chosen_item = inventory[intsell_input]
                item_price = sell_list.get(chosen_item, 0)
                if chosen_item in sell_list:
                    print(
                        f"Deal.   You sold {chosen_item} for {item_price} (yoohooo im rich)"
                    )
                    inventory.pop(intsell_input)
                    gold += item_price
                elif chosen_item not in sell_list:
                    print("I dont buy rubbish, fuck off you donkey! (Out of range)")
        else:
            print("Buddy, it needs to be a FUCKING DIGIT (Out of range)")
    else:
        print("Out of range")

    return inventory, gold


def fight_mechanic(inventory, health, gold, weaponList, consumableList):

    import random

    enemy = {
        "Goblin": {"hp": 50, "loot": "Goblin Flesh", "gold": 25, "dmg": 15},
        "Baby Goblin": {"hp": 15, "loot": "Goblin Eyes", "gold": 10, "dmg": 5},
    }

    enemy_rng = 20  # This is the miss chance for the enemy when they fight back, for now this applies to every enemies but will soon be changed

    for weapon in weaponList:
        has_weapon = False
        if weapon in inventory:
            has_weapon = True
            break
        else:
            has_weapon = False

    if has_weapon:
        print("Are you sure you want to fight? Y/N (holy ur buff man)")
        startfight = str(input())

        if startfight == "Y" or startfight == "y":
            random_enemy = random.choice(list(enemy.keys()))
            enemy_hp = enemy[random_enemy]["hp"]
            enemy_dmg = enemy[random_enemy]["dmg"]

            loot_drop = enemy[random_enemy]["loot"]
            gold_drop = enemy[random_enemy]["gold"]

            print(f"Theres a {random_enemy}!")
            print(f"HP: {enemy_hp}")
            print("Press 1 attack, 2 open inventory, 0 retreat")

            while enemy_hp > 0 and health > 0:
                fight_input = input()
                if fight_input.isdigit():
                    intfight = int(fight_input)
                    if intfight == 1:
                        enemy_hp -= random.randint(8, 12)
                        print(f"Enemy:  {random_enemy, enemy_hp}")
                        if enemy_hp >= 0:
                            rng = random.randint(1, 100)
                            if rng > enemy_rng:
                                health -= enemy_dmg
                                print(f"Boi you got damaged by -{enemy_dmg}")
                                print(f"You:    {health}")
                            elif rng <= enemy_rng:
                                print(f"The {random_enemy} missed (phew..)")
                                print(f"You:    {health}")
                    elif intfight == 2:
                        print(inventory)
                        player_input = input()
                        if player_input.isdigit:
                            intplayer_input = int(player_input)
                            if intplayer_input < 0 or intplayer_input >= len(inventory):
                                print("Out of range lil bro")
                            else:
                                print(inventory[intplayer_input])
                                inventory, health = use_item(
                                    intplayer_input,
                                    inventory,
                                    health,
                                    weaponList,
                                    consumableList,
                                )
                                print("Health:  ", health)
                        else:
                            print(
                                "Out of range (must be a number how tf have you not learnt by now)"
                            )
                    elif intfight == 0:
                        print(
                            f"You ran away! (imagine running away from a {random_enemy} lmao)"
                        )
                        break
                    else:
                        print("Out of range (Buddy, just press 1 or 0 what's so hard)")

                else:
                    print("Out of range (not a digit dummy)")

            if enemy_hp <= 0:
                print(f"You killed the {random_enemy}!")
                inventory.append(loot_drop)
                gold += gold_drop

                print(f"You got:    {loot_drop} and {gold_drop} Gold")

            elif health <= 0:
                print(f"you died bro imagine dying to a {random_enemy} xD")

        elif startfight == "N" or startfight == "n":
            print("Canceled (weakling)")

        else:
            print("Out of range")

    elif not has_weapon:
        print("Buddy you can't fight without a weapon (lmao)")

    else:
        print("Out of range (weirdo)")

    return inventory, health, gold


main()
