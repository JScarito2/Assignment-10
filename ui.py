class Colors:
    GREEN = '\033[92m'    # Success / Health / Rewards
    YELLOW = '\033[93m'   # Gold / Items / Quests
    RED = '\033[91m'      # Monsters / Bosses / Alerts
    BLUE = '\033[94m'     # NPCs / Narratives
    CYAN = '\033[96m'     # Menus / UI Elements
    END = '\033[0m'       # Reset color

def display_menu(title, options):
    print(f"\n{Colors.CYAN}=== {title.upper()} ==={Colors.END}")
    for key, val in options.items():
        print(f"[{key}] {val}")
    print(f"{Colors.CYAN}==================={Colors.END}")

def print_text(text, color=Colors.END):
    print(f"{color}{text}{Colors.END}")
