
import time
from ui import print_text, Colors

def show_intro():
    print_text("\n=== STORY INTRODUCTION ===", Colors.BLUE)
    intro_lines = [
        "Darkness has swept across the kingdom of Eldoria.",
        "The Dread Overlord Malakor has stolen the Eternal Flame.",
        "Monsters roam the wilds, terrorizing peaceful villages.",
        "You emerge from exile with nothing but a sword and a destiny...",
        "To defeat the Overlord, you must forge alliances and grow stronger!"
    ]
    for line in intro_lines:
        print_text(line, Colors.BLUE)
        time.sleep(0.5)
    print_text("===========================\n", Colors.BLUE)

def show_victory():
    print_text("\n" + "#" * 40, Colors.GREEN)
    print_text("CONGRATULATIONS! YOU HAVE DEFEATED THE FINAL BOSS!", Colors.GREEN)
    print_text("The Eternal Flame has been restored to Eldoria.", Colors.GREEN)
    print_text("Your name will be sung by bards for centuries to come.", Colors.GREEN)
    print_text("#" * 40 + "\n", Colors.GREEN)
