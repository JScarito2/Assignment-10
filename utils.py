# utils.py
def prompt_choice(min_val, max_val):
    while True:
        choice = input("Enter your option selection: ").strip()
        if choice.isdigit() and min_val <= int(choice) <= max_val:
            return int(choice)
        print("Invalid selection choice. Try again.")
