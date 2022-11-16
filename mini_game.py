command = ''
fight_start = False
player_hp = 100
player_damage = 51
npc_hp = 100
npc_damage = 12
level = 1
exp = 0
exp_gain = 50
run_damage = 20
mine_level = 1
mine_exp = 0
fish_lvl = 1
fish_exp = 0

while command.lower() != 'quit':
    print("Type 'help' for list of commands!")
    command = input("> ")
    #Combat
    if command.lower() == 'fight':
        fight_start = True
        print("Fight Has Begun!")
        while fight_start == True:
            option = input("Attack? y/n: ")
            if player_hp <= 0 and npc_hp >= 0:
                player_hp = 100
                npc_hp = 100
                exp = exp - 10
                print("You Have Died!")
                print("You lost 10xp!")
                print(f"Experience: {exp}")
                fight_start = False
            elif npc_hp <= 0 and player_hp >= 0:
                npc_hp = 100
                exp = exp + exp_gain
                print("You have slain the monster!")
                print(f"You have gained {exp_gain}xp!")
                print(f"Level: {level} - Experience: {exp}/100")
                fight_start = False
        #Character Level-Up
            while exp >= 100:
                level = level + 1
                player_hp = 100
                print(f"You have leveled up to level {level}!")
                exp = 0
            if option.lower() == 'y':
                npc_hp = npc_hp - player_damage
                player_hp = player_hp - npc_damage
                print(f"You Dealt {player_damage} Damage!")
                print(f"The monster dealt {npc_damage} damage!")
                print(f"Player HP:{player_hp}")
                print(f"NPC HP: {npc_hp}")
                if player_hp <= 0 and npc_hp >= 0:
                    player_hp = 100
                    npc_hp = 100
                    exp = exp - 10
                    print("You Have Died!")
                    print("You lost 10xp!")
                    print(f"Experience: {exp}/100")
                    fight_start = False
            elif option.lower() == 'n':
                player_hp = player_hp - run_damage
                print("You ran from the fight...")
                print("The monster attacked you from behind in the process of fleeing...")
                print(f"You took {run_damage} damage!")
                print(f"Player HP: {player_hp}")
                fight_start = False
            else:
                print("Please enter 'Y' or 'N'!")
# Heal - Heals player + 10
    elif command.lower() == 'heal':
        player_hp = player_hp + 10
        print("You have used a health potion! +10hp")
        print(f"Player HP: {player_hp}")
#Plevel - Displays level - exp
    elif command.lower() == 'plevel':
        print(f"Level: {level} - {exp}/100")
#Mining
    elif command.lower() == 'mine':
        mine_exp = mine_exp + 20
        print("You mined some rocks!")
        print(f"You received +20xp! - {mine_exp}/100")
        while mine_exp >= 100:
            print("You have leveled up in mining!")
            mine_level = mine_level + 1
            print(f"Mining Level: {mine_level} - {mine_exp}/100")
            mine_exp = 0
#Fishing
    elif command.lower() == 'fish':
        print("You cast your bait into the water...")
        fish_exp = fish_exp + 25
        print("You didn't catch anything. But you still received some exp!")
        print(f"Fishing Level: {fish_lvl} - Exp: {fish_exp}/100")
        while fish_exp >= 100:
            print("You have leveled up in your fishing level!")
            fish_lvl = fish_lvl + 1
            print(f"You are now level {fish_lvl} in fishing!")
            fish_exp = 0


    elif command.lower() == 'quit':
        break
    elif command.lower() == 'help':
            print("""
            *COMBAT*------------------------------------------
            Fight - Starts a Fight With an NPC
            Heal - Heals Player for 10hp
            Plevel - Displays current level, and amount of EXP for character. 
            
            *SKILLS*------------------------------------------
            Mine - Mines some rocks.
            
            *SETTINGS/EXIT*-------------------------------------
            Quit - Exit the Game
            Help - Prints list of Commands
            """)
    else:
        print("Please enter a valid command!")