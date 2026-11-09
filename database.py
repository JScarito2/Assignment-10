from tinydb import TinyDB, Query

db = TinyDB("game_saves.json")
users_table = db.table("users")

def find_user(username):
    User = Query()
    result = users_table.search(User.username == username)
    return result[0] if result else None

def create_user(username, password):
    default_data = {
        "username": username,
        "password": password,
        "level": 1,
        "exp": 0,
        "gold": 20,
        "inventory": ["Rusty Sword", "Health Potion"],
        "main_quest_step": 1,  # 1 = Start, 2 = Ready for Boss, 3 = Defeated Boss (Game Won)
        "side_quests_completed": []
    }
    users_table.insert(default_data)
    return default_data

def save_user_state(player_data):
    User = Query()
    users_table.update(player_data, User.username == player_data["username"])
