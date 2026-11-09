# combat.py
import random
from ui import print_text, Colors

# 5 Monster types with explicit scaling
MONSTERS = [
    {"name": "Scout Goblin", "hp": 25, "atk": 5, "boss": False},
    {"name": "Forest Slime", "hp": 15, "atk": 3, "boss": False},
    {"name": "Rabid Wolf", "hp": 30, "atk": 8, "boss": False},
    {"name": "Undead Soldier", "hp": 45, "atk": 10, "boss": False},
    {"name": "Dread Overlord Malakor", "hp": 100, "atk": 18, "boss": True}
]

def engage_battle(player_obj, target_monster_name):
    monster = next(m for m in MONSTERS if m["name"] == target_monster_name).copy()
    player_hp = 30 + (player_obj.data["level"] * 10)
    
    print_text(f"\nAn enemy draws near: {monster['name']}!", Colors.RED)
    
    while player_hp > 0 and monster["hp"] > 0:
        print(f"\nYour HP: {player_hp} | {monster['name']} HP: {monster['hp']}")
        action = input("Actions: [A]ttack or [R]un: ").strip().lower()
        
        if action == 'r':
            if monster["boss"]:
                print_text("You cannot run away from the Final Boss!", Colors.RED)
                continue
            print_text("You fled back to the safety of the town!", Colors.YELLOW)
            return False
            
        if action == 'a':
            # Player swing
            dmg = random.randint(8, 15) + player_obj.data["level"]
            if "Epic Sword" in player_obj.data["inventory"]:
                dmg += 10
            monster["hp"] -= dmg
            print_text(f"You strike the {monster['name']} for {dmg} damage!", Colors.GREEN)
            
            if monster["hp"] <= 0:
                break
                
            # Monster retaliates
            m_dmg = random.randint(3, monster["atk"])
            player_hp -= m_dmg
            print_text(f"The {monster['name']} hits you back for {m_dmg} damage!", Colors.RED)

    if player_hp <= 0:
        print_text("You were knocked out! Rest up and try again.", Colors.RED)
        return False
    else:
        print_text(f"Victory! You defeated {monster['name']}.", Colors.GREEN)
        return True
