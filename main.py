# main.py
import auth
import story
import npc
import combat
import quests
import utils
from player import Player
from ui import display_menu, print_text, Colors

def main():
    player_data = auth.authenticate()
    if not player_data:
        print_text("Goodbye!", Colors.CYAN)
        return

    player = Player(player_data)

    # Show introduction story if it is a brand new save account
    if player.data["main_quest_step"] == 1 and player.data["exp"] == 0:
        story.show_intro()

    while True:
        # Check overall win condition
        if player.data["main_quest_step"] == 3:
            story.show_victory()
            break

        menu_opts = {
            "1": "View Hero Profile Stats",
            "2": "Talk to Town NPCs (5 available)",
            "3": "Check Active Quest logs",
            "4": "Embark on Side Quest 1 (Slime Hunt)",
            "5": "Embark on Side Quest 2 (Wolf Menace)",
            "6": "Confront Final Boss (Main Quest)",
            "7": "Grind standard mobs (Goblins/Undead)",
            "8": "Save progress and Quit Game"
        }
        display_menu("Town Square Hub", menu_opts)
        
        choice = input("What do you want to do? ").strip()

        if choice == "1":
            player.show_stats()
            
        elif choice == "2":
            print("\nSelect an NPC to talk to:")
            for k, v in npc.NPC_DATA.items():
                print(f"[{k}] {v['name']}")
            npc_choice = input("Choose NPC ID: ").strip()
            spoken_npc = npc.talk_to_npc(npc_choice)
            
            # Advancing Main Quest line if talking to the Elder
            if spoken_npc == "Village Elder Alistair" and player.data["main_quest_step"] == 1:
                player.data["main_quest_step"] = 2
                print_text("\n[Main Quest Updated!] You are now cleared to hunt the Boss.", Colors.YELLOW)
                player.gain_rewards(20, 10)
                
        elif choice == "3":
            quests.check_quests(player)
            
        elif choice == "4":
            quests.run_side_quest_1(player)
            
        elif choice == "5":
            quests.run_side_quest_2(player)
            
        elif choice == "6":
            if player.data["main_quest_step"] < 2:
                print_text("You haven't even found out where the boss resides. Talk to the Elder first!", Colors.RED)
            else:
                print_text("\nYou scale the Volcanic Spire to challenge Overlord Malakor...", Colors.RED)
                if combat.engage_battle(player, "Dread Overlord Malakor"):
                    player.data["main_quest_step"] = 3  # Triggers victory loop
                    
        elif choice == "7":
            enemy = "Undead Soldier" if player.data["level"] >= 3 else "Scout Goblin"
            if combat.engage_battle(player, enemy):
                player.gain_rewards(30, 10)
                
        elif choice == "8":
            print_text("Saving game state database... Goodbye adventurer!", Colors.GREEN)
            break
        else:
            print_text("Invalid action choice selected.", Colors.RED)

if __name__ == "__main__":
    main()
