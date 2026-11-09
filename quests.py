# quests.py
from ui import print_text, Colors
import combat

def check_quests(player_obj):
    print_text("\n--- QUEST LOG ---", Colors.CYAN)
    
    # 1 Multi-step Main Quest status
    m_step = player_obj.data["main_quest_step"]
    if m_step == 1:
        print("- Main Quest Step 1: Speak to Village Elder Alistair to learn about the Overlord.")
    elif m_step == 2:
        print("- Main Quest Step 2: Slay Dread Overlord Malakor at the Volcanic Spire!")
    else:
        print("- Main Quest Completed: Peace is restored.")

    # 2 Side Quests status
    sides = player_obj.data["side_quests_completed"]
    if "Side Quest 1" not in sides:
        print("- Side Quest 1: Hunt the Slime in the woods for Alchemist Sarah.")
    if "Side Quest 2" not in sides:
        print("- Side Quest 2: Clear the Farm of the Rabid Wolf for Blacksmith Brokk.")

def run_side_quest_1(player_obj):
    if "Side Quest 1" in player_obj.data["side_quests_completed"]:
        print_text("You have already finished this side quest!", Colors.YELLOW)
        return
    
    print_text("\nRunning Side Quest: Gathering materials for Sarah...", Colors.YELLOW)
    if combat.engage_battle(player_obj, "Forest Slime"):
        player_obj.data["side_quests_completed"].append("Side Quest 1")
        # Rewards include gold, exp, or items
        player_obj.gain_rewards(exp=40, gold=15, item="Slime Core")

def run_side_quest_2(player_obj):
    if "Side Quest 2" in player_obj.data["side_quests_completed"]:
        print_text("You have already finished this side quest!", Colors.YELLOW)
        return
        
    print_text("\nRunning Side Quest: Defending the farm gates...", Colors.YELLOW)
    if combat.engage_battle(player_obj, "Rabid Wolf"):
        player_obj.data["side_quests_completed"].append("Side Quest 2")
        # Rewards include gold, exp, or items
        player_obj.gain_rewards(exp=60, gold=30, item="Epic Sword")
