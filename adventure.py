"""Week 4 Coding Assignment: Kyani's Adventure - part 4"""
import random

#display_player_status fucntion
def display_player_status(player_health):
    """Displays the player's health"""
    print(f"Your current health: {player_health}")

#acquire_item function
def acquire_item(inventory,item):
    """"Just puts items into inventory"""
    inventory.append(item)
    print(f"You acquired a {item}!")
    return inventory

#display_inventory function
def display_inventory(inventory):
    """"Displays the inventory"""
    if len(inventory)== 0:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        #will display the inventory, using enumereate() to count items
        for index,value in enumerate(inventory):
            print(f"{index + 1}. {value}")

# handle_path_choice function
def handle_path_choice(player_health):
    """Performs actions when user makes a change in direction"""
    path_choices = ['left','right']
    path_chosen = random.choice(path_choices)
    if path_chosen == 'left':
        print("You encounter a friendly gnome who heals you for 10 health points!")
        new_health = player_health + 10
        if new_health>= 100:
            player_health = 100
        elif new_health < 100:
            player_health = new_health
    elif path_chosen == 'right':
        print("You fall into a pit and lose 15 health points!")
        new_health = player_health - 15
        if new_health <= 0:
            print("You are barely alive!")
        else:
            player_health = new_health
    return player_health

#player_attack function
def player_attack(monster_health):
    """You hit the monster"""
    print("You strike the monster for 15 damage!")
    #set a max function to ensure that monster_health never goes under 0
    monster_health = max(0, monster_health - 15)
    return monster_health

#monster_attack function
def monster_attack(player_health):
    """The monster hits you"""
    normal_attack = player_health - 10
    critical_hit = player_health - 20
    if random.random() <0.5: #50% chance of critical hit
        player_damage = critical_hit
        print("The monster lands a critical hit for 20 damaage")
    else:
        player_damage = normal_attack
        print("The monster hits you for 10 damage!")
    #using max function to ensure player_health doesnt become negative
    #once player_damage is introduced
    player_health = max(0, player_damage)
    return player_health

#combat_encounter function
def combat_encounter(player_health, monster_health, has_treasure):
    """Changes in player health when attacked by monster"""
    while player_health > 0 and monster_health > 0:
        monster_gets_hit = player_attack(monster_health)
        monster_health = monster_gets_hit
        display_player_status(player_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            if has_treasure:
                print("Under the monster you find a mysterious haunted treasure...")
                return True,player_health #Player won and there was treasure
            return False,player_health #Player won but no treasure :/
            #inserted break statements with the return function if there's no treasure
        player_gets_hit = monster_attack(player_health)
        player_health = player_gets_hit
        display_player_status(player_health)
        if player_health <= 0:
            print("Game Over!")
    return False,player_health #Player lost AND no treasure :/
    #inserted break statement with the return if we lose

#check_for_treasure function
def check_for_treasure(has_treasure):
    """Checks for treasure"""
    if has_treasure:
        print("You found the hidden treasure! You've won your first monster encounter!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

#enter_dungeon function
def enter_dungeon(player_health,inventory, dungeon_rooms):
    """You enter the dungeon"""
    random.shuffle(dungeon_rooms)
    for dungeon_room in dungeon_rooms: #this is the protocol for every room when it has been entered
        print(dungeon_room[0]) #when they enter a room, they will say the room's description first
        if dungeon_room[1] is not None:
            #update the inventory every time an item from a dungeon room is acquired
            inventory = acquire_item(inventory, dungeon_room[1])
            print("You found a", dungeon_room[1], "in the room.")
        if dungeon_room[2]== 'puzzle': #Everything that happends when you encounter a puzzle
            print("You encounter a puzzle!")
            puzzle_ask = input("Do you wish to solve it? or skip?: ")
            if puzzle_ask == 'solve':
                puzzle_decision = random.choice([True,False])
                if puzzle_decision:
                    print(dungeon_room[3][0]) #prints success message
                    health_change = dungeon_room[3][2]
                    player_health = max(0, player_health + health_change)
                    if player_health == 0:
                        print("You are barely alive!")
        elif dungeon_room[2]== 'trap':
            print("You see a potential trap!")
            trap_ask = input("Do you wish to disarm or bypass it?: ")
            if trap_ask == 'disarm':
                trap_decision = random.choice([True,False])
                if trap_decision: #they successfully disarm
                    print(dungeon_room [3][0]) #prints success message
                else:
                    print(dungeon_room [3][1]) #prints failure message
                health_change = dungeon_room[3][2]
                player_health = max(0, player_health + health_change)
                if player_health == 0:
                    print("You are barely alive!")
        else:
            print("There doesn't seem to be a challenge in this room. You move on")
        display_inventory(inventory)
        display_player_status(player_health)
    return player_health,inventory
#end of enter_dungeon function - its really long :)

def main():
    """The main function"""
    player_health = 100
    monster_health = 60
    inventory = [] #everything should be initialized before first function is called
    dungeon_rooms = [
        ('\nYou enter the Tunnel of Barador \n A giant fortress laced in Ice and Silver',
         'None','trap', ('You have made it out alive!', 'You were caught in a trap!', -15)),
        ('\nYou enter the Enchanted Cave of Mystery \nA gem filled cave filled with puzzles',
         'key','puzzle', ('You solved the puzzle!', 'The puzzle will remains unsolved', -5)),
        ('\nYou have stumbled upon a room with a small cauldron \n It is the Elixir of Life!',
         'potion', 'none', None),
        ('\nYou found a room with a treasure chest! But look there is a puzzle...',
         'treasure','puzzle', ('You solved the puzzle!','Door remains stubbornly locked', -5))]
    display_player_status(player_health)
    boolean_choices = [True,False]
    has_treasure = random.choice(boolean_choices)

#updates player_health and says the current health has changed after this function
    player_health = handle_path_choice(player_health)
    display_player_status(player_health)
    fight,updated_health = combat_encounter(player_health, monster_health, has_treasure)
    #fight means if the player won and the monster had the treasure
    check_for_treasure(fight)
    #says that in the event that fight is happening, do the check for treasure stuff
    updated_health,updated_inventory = enter_dungeon(updated_health, inventory, dungeon_rooms)
    display_inventory(updated_inventory) #displays updated inventory after dungeon exploration
    display_player_status(updated_health) #displays updated health after dungeon exploration

    if updated_health > 0:
        #This means that the user has SURVIVED the combat encounter, go explore dungeons
        print("Congratulations! You have survived exploring the dungeon rooms, you've won! ")
    else:
        print("You did not survive the dungeon. Game Over!")
    player_health = updated_health
if __name__ == '__main__':
    main()
