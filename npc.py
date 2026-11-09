# npc.py
from ui import print_text, Colors

NPC_DATA = {
    "1": {
        "name": "Village Elder Alistair",
        "dialogue": "Young hero, the Overlord Malakor rules from the Volcanic Spire. Go build your strength!"
    },
    "2": {
        "name": "Blacksmith Brokk",
        "dialogue": "Need a sharper edge? Clean out those pests at the farm and I'll see what I can forge."
    },
    "3": {
        "name": "Alchemist Sarah",
        "dialogue": "Be careful out there! A strange slime core from the woods could help me brew wonderful potions."
    },
    "4": {
        "name": "Guard Captain Rayna",
        "dialogue": "Stay alert. The paths outside town are crawling with vicious wildlife."
    },
    "5": {
        "name": "Mysterious Hermit",
        "dialogue": "Heh... looking to win? Don't challenge Malakor unless you have an Epic weapon!"
    }
}

def talk_to_npc(npc_id):
    if npc_id in NPC_DATA:
        npc = NPC_DATA[npc_id]
        print_text(f"\n[{npc['name']}]: '{npc['dialogue']}'", Colors.BLUE)
        return npc['name']
    return None
