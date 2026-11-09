# player.py
import database
from ui import print_text, Colors

class Player:
    def __init__(self, data):
        self.data = data

    def show_stats(self):
        print_text(f"\n--- {self.data['username']}'s Character Status ---", Colors.CYAN)
        print(f"Level: {self.data['level']} | EXP: {self.data['exp']}/100")
        print_text(f"Gold: {self.data['gold']}", Colors.YELLOW)
        print(f"Inventory: {', '.join(self.data['inventory'])}")
        print(f"Main Quest Progress Step: {self.data['main_quest_step']}")
        print(f"Side Quests Completed: {len(self.data['side_quests_completed'])}/2")

    def gain_rewards(self, exp, gold, item=None):
        self.data['exp'] += exp
        self.data['gold'] += gold
        print_text(f"[+] Gained {exp} EXP and {gold} Gold!", Colors.GREEN)
        if item:
            self.data['inventory'].append(item)
            print_text(f"[+] Found Item: {item}!", Colors.YELLOW)
        
        if self.data['exp'] >= 100:
            self.data['level'] += 1
            self.data['exp'] -= 100
            print_text(f"LEVEL UP! You are now Level {self.data['level']}!", Colors.GREEN)
        
        database.save_user_state(self.data)
